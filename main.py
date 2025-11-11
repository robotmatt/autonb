from seleniumSetup import *
from browserSetup import *
from basicRun import *
from complexRun import *
from config import *

# time between keypresses (0.25 is a known good number)
timeBetween = 0.025

browser = seleniumSetup()
browserSetup(browser, productionServer)
time.sleep(5)  # wait for the javascript to load

now = datetime.now()  # current date and time
date_time = now.strftime("%Y-%m-%d_%H:%M:%S")

if baselineTest == "CA" or baselineTest == "All":
    basicRun("TEST_low", date_time, ten_mil, "IAH", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
             verbose, 1)
    basicRun("TEST_low", date_time, ten_mil, "IAD", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
             verbose, 2)
    basicRun("TEST_mid", date_time, ten_mil, "IAH", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
             verbose, 3)
    basicRun("TEST_mid", date_time, ten_mil, "IAD", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
             verbose, 4)
    basicRun("TEST_high", date_time, ten_mil, "IAH", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
             verbose, 5)
    basicRun("TEST_high", date_time, ten_mil, "IAD", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
             verbose, 6)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAH", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser,
             testMode, verbose, 7)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAD", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser,
             testMode, verbose, 8)
elif baselineTest == "FO" or baselineTest == "All":
    basicRun("TEST_low", date_time, ten_mil, "IAH", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
             verbose, 1)
    basicRun("TEST_low", date_time, ten_mil, "IAD", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
             verbose, 2)
    basicRun("TEST_mid", date_time, ten_mil, "IAH", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
             verbose, 3)
    basicRun("TEST_mid", date_time, ten_mil, "IAD", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
             verbose, 4)
    basicRun("TEST_high", date_time, ten_mil, "IAH", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
             verbose, 5)
    basicRun("TEST_high", date_time, ten_mil, "IAD", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
             verbose, 6)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAH", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser,
             testMode, verbose, 7)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAD", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser,
             testMode, verbose, 8)
else:
    for base in baseList:
        for minThresholdHour in range(minFloor, minCeiling, 2):  # incrememnt the threshold hour between the floor and ceiling by 2
            for minThresholdMinute in range(0, 60, minThresholdIncrement):  # set the minute portion of the threshold. If set to (0, 60, 60) it will just do whole hours. If set to (0, 60, 30) then it will be 30 min increments. Can go as low as 15 minute increments.
                for maxThresholdHour in range(maxFloor, maxCeiling, 2):  # incrememnt the threshold hour between the floor and ceiling
                    for maxThresholdMinute in range(0, 60, maxThresholdIncrement):  # set the minute portion of the threshold. If set to (0, 60, 60) it will just do whole hours. If set to (0, 60, 30) then it will be 30 min increments. Can go as low as 15 minute increments.
                        for normalThresholdHour in range(normalFloor, normalCeiling):  # incrememnt the threshold hour between the floor and ceiling
                            for normalThresholdMinute in range(0, 60, normThresholdIncrement):  # set the minute portion of the threshold. If set to (0, 60, 60) it will just do whole hours. If set to (0, 60, 30) then it will be 30 min increments. Can go as low as 15 minute increments.
                                if minFloor <= normalFloor and minThresholdHour <= normalFloor:  # NAVBLUE won't let the min floor be greater than the normal floor
                                    if minFloor <= maxFloor and minThresholdHour <= maxFloor:  # NAVBLUE won't let the normal floor be greater than the max floor
                                        if normalFloor <= maxFloor and normalThresholdHour <= maxFloor:  # NAVBLUE won't let the normal floor be greater than the max floor
                                            # we don't want the normal threshold to ever be greater than max threshold. They can be equal though.
                                            if ((normalThresholdHour < maxThresholdHour) or (
                                                    (normalThresholdHour == maxThresholdHour) and (
                                                    normalThresholdMinute <= maxThresholdMinute))):
                                                # we don't want the min threshold to ever be greater than normal threshold. They can be equal though.
                                                if ((minThresholdHour < normalThresholdHour) or (
                                                        (minThresholdHour == normalThresholdHour) and (
                                                        minThresholdMinute <= normalThresholdMinute))):
                                                    basicRun(prefix, suffix, maxMinCredit, maxIterations, base, seat,
                                                             minFloor, minCeiling, minThresholdHour, minThresholdMinute,
                                                             normalFloor, normalCeiling, normalThresholdHour,
                                                             normalThresholdMinute, maxFloor, maxCeiling,
                                                             maxThresholdHour, maxThresholdMinute, split_low,
                                                             split_high, split_threshold, browser, testMode, verbose,
                                                             runcount)
                                                    runcount = runcount + 1
                                                else:
                                                    print("skipping run " + str(
                                                        runcount) + " because min threshold is greater than normal threshold")
                                            else:
                                                print("skipping run " + str(
                                                    runcount) + " because normal threshold is greater than max threshold")
                                        else:
                                            print("skipping run " + str(
                                                runcount) + " because normal floor is greater than max floor")
                                    else:
                                        print("skipping run " + str(
                                            runcount) + " because min floor is greater than max floor")
                                else:
                                    print("skipping run " + str(
                                        runcount) + " because min floor is greater than normal floor")
                        runcount = runcount + 1

print('**************')
print('Runs complete')
print('**************')
