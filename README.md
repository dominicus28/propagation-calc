# propagation-calc
Simple calculator calculating "beyond the horizon" propagation losses. 

Using model described in "Radiowave propagation and antennas for personal communications" K. Siwak, Y. Bahreini, chapter 7.4

For a dielectric constant value different from vaccum (epsilon = 1) or dry air (epsilon = 1.0006), it have to use float128 data type.
For this reason, program will run correctly only on Linux. On Windows 64-bit there is an issue with float128 data type - https://stackoverflow.com/questions/58686018/numpy-float128-doesnt-exist-in-windows-but-is-called-from-opengl
