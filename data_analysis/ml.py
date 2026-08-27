import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QComboBox, QTableWidget, QTableWidgetItem,
    QSizePolicy, QMessageBox, QSpinBox
)
from PySide6.QtCore import Qt

# ---------------------------------------------------------
# Factor Types:
# numeric-benefit  (higher is better)
# numeric-cost     (lower is better)
# categorical      (brand, os, color...) → User-defined scores
# ---------------------------------------------------------


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Criteria Ranking System")
        self.resize(1200, 750)

        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.factors = []
        self.factor_types = []
        self.factor_weights = []

        self.items = []
        self.num_factors = 0
        self.num_items = 0

        self.categorical_values = {}      # factor_index → list of unique raw categories
        self.categorical_scores = {}      # factor_index → dict{category: score}

        self.page_num_factors()
        self.stack.setCurrentIndex(0)

    # ---------------------------------------------------------
    # PAGE 1 — Number of Factors
    # ---------------------------------------------------------
    def page_num_factors(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        lbl = QLabel("Number of Factors:")
        self.input_factor_count = QSpinBox()
        self.input_factor_count.setMinimum(1)
        self.input_factor_count.setMaximum(50)
        btn = QPushButton("Next")
        btn.clicked.connect(self.goto_factor_names)

        layout.addWidget(lbl)
        layout.addWidget(self.input_factor_count)
        layout.addWidget(btn)
        layout.addStretch()

        self.stack.addWidget(w)

    # ---------------------------------------------------------
    # PAGE 2 — Factor Names, Types, Weights
    # ---------------------------------------------------------
    def goto_factor_names(self):
        self.num_factors = self.input_factor_count.value()

        w = QWidget()
        main = QVBoxLayout(w)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        form = QVBoxLayout(inner)

        self.factor_name_inputs = []
        self.factor_type_inputs = []
        self.factor_weight_inputs = []

        for i in range(self.num_factors):
            row = QHBoxLayout()

            name_edit = QLineEdit()
            name_edit.setPlaceholderText("Factor Name")

            type_box = QComboBox()
            type_box.addItems(
                ["numeric-benefit", "numeric-cost", "categorical"])

            weight_edit = QLineEdit()
            weight_edit.setPlaceholderText("Weight (e.g. 1.0)")

            self.factor_name_inputs.append(name_edit)
            self.factor_type_inputs.append(type_box)
            self.factor_weight_inputs.append(weight_edit)

            row.addWidget(name_edit)
            row.addWidget(type_box)
            row.addWidget(weight_edit)
            form.addLayout(row)

        scroll.setWidget(inner)
        main.addWidget(scroll)

        btn = QPushButton("Next")
        btn.clicked.connect(self.goto_num_items)
        main.addWidget(btn)

        self.stack.addWidget(w)
        self.stack.setCurrentWidget(w)

    # ---------------------------------------------------------
    # PAGE 3 — Number of Items
    # ---------------------------------------------------------
    def goto_num_items(self):
        try:
            self.factors = [f.text().strip() for f in self.factor_name_inputs]
            self.factor_types = [f.currentText()
                                 for f in self.factor_type_inputs]
            self.factor_weights = [float(w.text())
                                   for w in self.factor_weight_inputs]
        except:
            QMessageBox.warning(self, "Error", "Invalid weights.")
            return

        w = QWidget()
        layout = QVBoxLayout(w)

        lbl = QLabel("Number of Items:")
        self.input_item_count = QSpinBox()
        self.input_item_count.setMinimum(1)
        self.input_item_count.setMaximum(2000)

        btn = QPushButton("Next")
        btn.clicked.connect(self.goto_item_data)

        layout.addWidget(lbl)
        layout.addWidget(self.input_item_count)
        layout.addWidget(btn)
        layout.addStretch()

        self.stack.addWidget(w)
        self.stack.setCurrentWidget(w)

    # ---------------------------------------------------------
    # PAGE 4 — Item Data Entry
    # ---------------------------------------------------------
    def goto_item_data(self):
        self.num_items = self.input_item_count.value()

        w = QWidget()
        main = QVBoxLayout(w)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        form = QVBoxLayout(inner)

        self.item_name_inputs = []
        self.item_factor_inputs = []

        for _ in range(self.num_items):
            block = QVBoxLayout()

            name_edit = QLineEdit()
            name_edit.setPlaceholderText("Item Name")
            block.addWidget(name_edit)

            factor_entries = []
            for i in range(self.num_factors):
                h = QHBoxLayout()
                lbl = QLabel(self.factors[i] +
                             " (" + self.factor_types[i] + ") :")
                edit = QLineEdit()
                h.addWidget(lbl)
                h.addWidget(edit)
                block.addLayout(h)
                factor_entries.append(edit)

            self.item_name_inputs.append(name_edit)
            self.item_factor_inputs.append(factor_entries)

            form.addLayout(block)
            form.addSpacing(20)

        scroll.setWidget(inner)
        main.addWidget(scroll)

        btn = QPushButton("Next")
        btn.clicked.connect(self.extract_categorical_values)
        main.addWidget(btn)

        self.stack.addWidget(w)
        self.stack.setCurrentWidget(w)

    # ---------------------------------------------------------
    # Extract unique categorical values
    # ---------------------------------------------------------
    def extract_categorical_values(self):
        self.items = []
        for k in range(self.num_items):
            name = self.item_name_inputs[k].text().strip()
            if not name:
                QMessageBox.warning(self, "Error", "Empty item name.")
                return

            values = []
            for i in range(self.num_factors):
                raw = self.item_factor_inputs[k][i].text().strip()

                if self.factor_types[i] == "categorical":
                    values.append(raw)
                else:
                    try:
                        values.append(float(raw))
                    except:
                        QMessageBox.warning(self, "Error",
                                            f"Invalid numeric value for factor {self.factors[i]}.")
                        return

            self.items.append({"name": name, "values": values})

        self.categorical_values = {}
        for i in range(self.num_factors):
            if self.factor_types[i] == "categorical":
                vals = []
                for it in self.items:
                    v = it["values"][i]
                    if v not in vals:
                        vals.append(v)
                self.categorical_values[i] = vals

        self.page_categorical_scoring()

    # ---------------------------------------------------------
    # PAGE 5 — Assign score to all categorical options
    # ---------------------------------------------------------
    def page_categorical_scoring(self):
        w = QWidget()
        main = QVBoxLayout(w)

        self.categorical_score_inputs = {}  # factor → {category: input_box}

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        form = QVBoxLayout(inner)

        for i in range(self.num_factors):
            if self.factor_types[i] == "categorical":
                label = QLabel(f"Assign scores for factor: {self.factors[i]}")
                form.addWidget(label)

                self.categorical_score_inputs[i] = {}

                for cat in self.categorical_values[i]:
                    h = QHBoxLayout()
                    lbl = QLabel(cat + ":")
                    edit = QLineEdit()
                    h.addWidget(lbl)
                    h.addWidget(edit)
                    form.addLayout(h)
                    self.categorical_score_inputs[i][cat] = edit

                form.addSpacing(20)

        scroll.setWidget(inner)
        main.addWidget(scroll)

        btn = QPushButton("Calculate Ranking")
        btn.clicked.connect(self.save_categorical_scores)
        main.addWidget(btn)

        self.stack.addWidget(w)
        self.stack.setCurrentWidget(w)

    # ---------------------------------------------------------
    # Save user-defined categorical scores
    # ---------------------------------------------------------
    def save_categorical_scores(self):
        self.categorical_scores = {}

        for i in self.categorical_score_inputs:
            self.categorical_scores[i] = {}
            for cat, edit in self.categorical_score_inputs[i].items():
                try:
                    score = float(edit.text())
                except:
                    QMessageBox.warning(self, "Error",
                                        f"Invalid categorical score for {cat}.")
                    return
                self.categorical_scores[i][cat] = score

        self.rank_items()
        self.show_results()

    # ---------------------------------------------------------
    # Ranking with normalization + categorical weight
    # ---------------------------------------------------------
    def rank_items(self):
        matrix = []
        for it in self.items:
            row = []
            for j in range(self.num_factors):
                v = it["values"][j]
                if self.factor_types[j] == "categorical":
                    row.append(self.categorical_scores[j][v])
                else:
                    row.append(v)
            matrix.append(row)

        means = []
        for j in range(self.num_factors):
            col = [matrix[i][j] for i in range(self.num_items)]
            means.append(sum(col) / len(col))

        norm = []
        for r in range(self.num_items):
            row = []
            for j in range(self.num_factors):
                x = matrix[r][j]
                if self.factor_types[j] in ["numeric-benefit", "categorical"]:
                    row.append(x / means[j])
                else:
                    row.append(means[j] / x)
            norm.append(row)

        for idx in range(self.num_items):
            score = sum(self.factor_weights[j] * norm[idx][j]
                        for j in range(self.num_factors))
            self.items[idx]["score"] = score

        self.items.sort(key=lambda x: x["score"], reverse=True)

    # ---------------------------------------------------------
    # PAGE 6 — Results
    # ---------------------------------------------------------
    def show_results(self):
        w = QWidget()
        main = QVBoxLayout(w)

        table = QTableWidget()
        table.setColumnCount(self.num_factors + 2)
        headers = ["Item", "Score"] + self.factors
        table.setHorizontalHeaderLabels(headers)
        table.setRowCount(self.num_items)

        for r, it in enumerate(self.items):
            table.setItem(r, 0, QTableWidgetItem(it["name"]))
            table.setItem(r, 1, QTableWidgetItem(str(round(it["score"], 6))))

            for c in range(self.num_factors):
                table.setItem(r, 2 + c, QTableWidgetItem(str(it["values"][c])))

        table.resizeColumnsToContents()
        main.addWidget(table)

        self.stack.addWidget(w)
        self.stack.setCurrentWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec())
