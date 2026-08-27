import numpy as np
import matplotlib.pyplot as plt

"""
#plot 11
# تعریف تابع 
def f_nearestneighbor_int(x, xdata, fdata):
    ind = np.searchsorted(xdata, x)
    
    
    if (ind == 0):
        return fdata[0]
    if (ind == len(xdata)):
        return fdata[-1]
    
    x0, f0 = xdata[ind-1], fdata[ind-1]
    x1, f1 = xdata[ind], fdata[ind]
    
    # منطق نزدیک‌ترین همسایه
    if (abs(x - x0) < abs(x - x1)):
        return f0
    else:
        return f1

# ساخت دیتاهای مورد نیاز 
xdat = np.array([0, 1, 2, 3, 4, 5, 6])
fdat = np.sin(xdat)

# محاسبات برای رسم نمودار
xcalc = np.linspace(0, 6, 500) # شبکه دقیق‌تر برای نمایش پله‌ها
fcalc = [f_nearestneighbor_int(xin, xdat, fdat) for xin in xcalc]

# ساخت تابع اصلی 
xtrue = np.linspace(0, 6, 200)
ftrue = np.sin(xtrue)

# رسم نمودار
plt.figure(figsize=(8, 6))

# رسم نقاط داده
plt.plot(xdat, fdat, 'ro', label='data', markersize=6, markeredgecolor='gray')
plt.plot(xcalc, fcalc, '-', label='nearest-neighbor interpolation', color='#4C72B0')

# رسم تابع اصلی 
plt.plot(xtrue, ftrue, '--', label='true function', color='#DD8452')

# تنظیمات ظاهری 
plt.title('Nearest-neighbor interpolation')
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc='lower left')
plt.ylim(-1.1, 1.1) # محدوده محور y برای وضوح بیشتر
plt.show()
"""


"""
#plot 12
def linear_int(x, x0, f0, x1, f1):
    return f0 + (f1 - f0) * (x - x0) / (x1 - x0)

def f_linear_int(x, xdata, fdata):
    ind = np.searchsorted(xdata, x) # Search the right interval for point x
    
    if (ind == 0):
        if ((xdata[0] - x) > 1e-12):
            print("x = ", x, " is outside the interpolation range [",xdata[0],",",xdata[-1],"]")
        ind = ind + 1
        
    if (ind == len(xdata)):
        if ((x - xdata[-1]) > 1e-12):
            print("x = ", x, " is outside the interpolation range [",xdata[0],",",xdata[-1],"]")
        ind = ind - 1
        
    x0, f0 = xdata[ind-1], fdata[ind-1]
    x1, f1 = xdata[ind], fdata[ind]
    return linear_int(x, x0, f0, x1, f1)

# تعریف دیتا مشابه مرحله قبل
xdat = np.array([0, 1, 2, 3, 4, 5, 6])
fdat = np.sin(xdat)

# محاسبه مقادیر درونیابی خطی
xcalc = np.linspace(0, 6, 100)
fcalc = [f_linear_int(xin, xdat, fdat) for xin in xcalc]

# رسم نمودار
plt.figure(figsize=(8, 5))
plt.plot(xdat, fdat, 'ro', label='data') # نقاط قرمز
plt.plot(xcalc, fcalc, '-', label='linear interpolation') # خطوط آبی
plt.plot(np.linspace(0, 6, 100), np.sin(np.linspace(0, 6, 100)), '--', label='true function') # خط‌چین نارنجی
plt.title('Linear interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
"""


"""
#plot 13
def Lnj(x, n, j, xdata):

    ret = 1.
    for k in range(0, len(xdata)):
        if (k != j):
            ret *= (x - xdata[k]) / (xdata[j] - xdata[k])
    return ret

def f_poly_int(x, xdata, fdata):

    ret = 0.
    n = len(xdata) - 1
    for j in range(0, n + 1):
        ret += fdata[j] * Lnj(x, n, j, xdata)
    return ret



# تعریف نقاط گسسته 
xdat = np.array([0, 1, 2, 3, 4, 5, 6])
fdat = np.sin(xdat)

# ایجاد شبکه نقاط برای رسم نمودار 
xpoly = np.linspace(0, 6, 200)
fpoly = np.array([f_poly_int(xin, xdat, fdat) for xin in xpoly])

# تابع واقعی برای مقایسه 
ftrue = np.sin(xpoly)

# محاسبه خطا 
error = np.abs(fpoly - ftrue)



fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={'height_ratios': [1.2, 1]})

# نمودار بالا: نمایش درونیابی
ax1.plot(xdat, fdat, 'ro', label='data')
ax1.plot(xpoly, fpoly, '-', label='polynomial interpolation', color='#4C72B0')
ax1.plot(xpoly, ftrue, '--', label='true function', color='#DD8452')
ax1.set_title('Polynomial interpolation')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.legend()

# نمودار پایین: نمایش خطا
ax2.plot(xpoly, error, '--', label='error', color='#4C72B0')
ax2.set_title('Polynomial interpolation error')
ax2.set_xlabel('x')
ax2.set_ylabel('|p(x) - sin(x)|')
ax2.legend()

plt.tight_layout()
plt.show()
"""
