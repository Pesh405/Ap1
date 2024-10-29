import os
import sys


recordUrl = sys.argv[1]


def main():
    print(str(recordUrl))
    recordUrlArr = recordUrl.split('_')
    screenWidth = recordUrlArr[1]
    screenHeight = recordUrlArr[2]
    screenDensity = recordUrlArr[3]


    os.system('adb devices')
    out1 = os.popen('adb shell wm size ' + screenWidth + 'x' + screenHeight).read()
    out2 = os.popen('adb shell wm density ' + screenDensity).read()
    out3 = os.popen('adb shell am start -n easy.sudoku.puzzle.solver.free/com.meevii.ui.activity.SplashActivity --es recordUrl ' + recordUrl).read()
    print(out1)
    print(out2)
    print(out3)


if __name__ == '__main__':
    main()