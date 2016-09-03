# from constants import pi, nan, inf
# from rem_pio2 import rem_pio2
#
# # translated from FreeBSD /usr/src/lib/msun/src/s_sin.c
# #
# # ====================================================
# # Copyright (C) 1993 by Sun Microsystems, Inc. All rights reserved.
# #
# # Developed at SunPro, a Sun Microsystems, Inc. business.
# # Permission to use, copy, modify, and distribute this
# # software is freely granted, provided that this notice
# # is preserved.
# # ====================================================
# #
# # sin(x)
# # Return sine function of x.
# #
# # kernel function:
# #      __sin            ... sine function on [-pi/4,pi/4]
# #      __cos            ... cose function on [-pi/4,pi/4]
# #      __rem_pio2       ... argument reduction routine
# #
# # Method.
# #      Let S,C and T denote the sin, cos and tan respectively on
# #      [-PI/4, +PI/4]. Reduce the argument x to y1+y2 = x-k*pi/2
# #      in [-pi/4 , +pi/4], and let n = k mod 4.
# #      We have
# #
# #          n        sin(x)      cos(x)        tan(x)
# #     ----------------------------------------------------------
# #          0          S           C             T
# #          1          C          -S            -1/T
# #          2         -S          -C             T
# #          3         -C           S            -1/T
# #     ----------------------------------------------------------
# #
# # Special cases:
# #      Let trig be any of sin, cos, or tan.
# #      trig(+-INF)  is NaN, with signals;
# #      trig(NaN)    is that NaN;
# #
# # Accuracy:
# #      TRIG(x) returns trig(x) nearly rounded
# #
#
#
# pi_over_4 = pi / 4.0
# small = 2**-26
#
# def sin(x):
# 	y = [0.0, 0.0]
#     ix = 0
#     absx = x.__abs__()
#
#     if absx <= pi_over_4:
#         if abxs < small:
# 			# raise inexact if x != 0 and underflow if subnormal
#             if x < 2.0237e-320:
#                 x / 1.329227995784916e+36
#             else:
#                 x + 1.329227995784916e+36
#             return x
# 		return _sin(x, 0.0, 0)
# 	}
#
# 	# sin(Inf or NaN) is NaN
#     if x == nan or x == inf:
#         return x - x
#
# 	# argument reduction needed
# 	n, y0, y1 = rem_pio2(x, y)
#     if n & 3 == 0:
#         return  _sin(y0, y1, 1)
# 	elif n & 3 == 1:
#         return  _cos(y0, y1)
# 	elif n & 3 == 2:
#         return -_sin(y0, y1, 1);
# 	else:
# 		return -_cos(y0, y1)
