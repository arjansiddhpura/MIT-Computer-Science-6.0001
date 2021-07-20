# Inferential Statistics

import random
from numpy import histogram_bin_edges
import pylab
import time


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads / numFlips


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    return mean


def regressToMean(numFlips, numTrials):
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i + 1])
    pylab.plot(range(len(extremes)), extremes, "ko", label="Extreme")
    pylab.plot(range(len(nextTrials)), nextTrials, "k^", label="Next Trial")
    pylab.axhline(0.5)
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)
    pylab.xlabel("Extreme Example and Next Trial")
    pylab.ylabel("Fraction Heads")
    pylab.title("Regression to the Mean")
    pylab.legend(loc="best")


# regressToMean(15, 50)
# pylab.show()


def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(("H", "T")) == "H":
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title("Difference between Heads and Tails")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Abs(#Heads - #Tails)")
    pylab.plot(xAxis, diffs, "ko")
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.title("Heads/Tails Ratios")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("#Heads/#Tails")
    pylab.plot(xAxis, ratios, "ko")
    pylab.semilogx()


# random.seed(0)
# flipPlot(4, 20)
# pylab.show()


def variance(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)


def stdDev(X):
    return variance(X) ** 0.5


def makePlot(xVals, yVals, title, xLabel, yLable, style, logX=False, logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLable)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


def runTrial(numFLips):
    numHeads = 0
    for n in range(numFLips):
        if random.choice(("H", "T")) == "H":
            numHeads += 1
    numTails = numFLips - numHeads
    return (numHeads, numTails)


def flipPlot1(minExp, maxExp, numTrials):
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    numTrialsString = " (" + str(numTrials) + " Trials)"
    title = "Mean Heads/Tails Ratios" + numTrialsString
    makePlot(
        xAxis,
        ratiosMeans,
        title,
        "Number of flips",
        "Mean Heads/Tails",
        "ko",
        logX=True,
    )
    title = "SD Heads/Tails Ratios" + numTrialsString
    makePlot(
        xAxis,
        ratiosSDs,
        title,
        "Number of FLips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )
    title = "Mean abs(#Heads - #Tails)" + numTrialsString
    makePlot(
        xAxis,
        diffsMeans,
        title,
        "Number of Flips",
        "Mean abs(#Heads - #Tails)",
        "ko",
        logX=True,
        logY=True,
    )
    title = "SD abs(#Heads - Tails)" + numTrialsString
    makePlot(
        xAxis,
        diffsSDs,
        title,
        "Number of Flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )


# # start_time = time.time()
# flipPlot1(4, 20, 20)
# # print("Calculated in %s seconds" % (time.time() - start_time))
# pylab.show()


def CV(X):
    mean = sum(X) / len(X)
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float("nan")


def flipPlot2(minExp, maxExp, numTrials):
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    ratiosCVs, diffsCVs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / float(numTails))
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = " (" + str(numTrials) + " Trials)"
    title = "Mean Heads/Tails Ratios" + numTrialsString
    makePlot(
        xAxis,
        ratiosMeans,
        title,
        "Number of flips",
        "Mean Heads Tails",
        "ko",
        logX=True,
    )
    title = "SD Heads/Tails Ratios" + numTrialsString
    makePlot(
        xAxis,
        ratiosSDs,
        title,
        "Number of flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )
    title = "Mean abs(#Heads - #Tails)" + numTrialsString
    makePlot(
        xAxis,
        diffsMeans,
        title,
        "Number of Flips",
        "Mean abs(#Heads - #Tails)",
        "ko",
        logX=True,
        logY=True,
    )
    title = "SD abs(#Heads - #Tails)" + numTrialsString
    makePlot(
        xAxis,
        diffsSDs,
        title,
        "Number of Flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )
    title = "Coeff. of Var. Heads/Tails Ratio" + numTrialsString
    makePlot(
        xAxis,
        ratiosCVs,
        title,
        "Number of Flips",
        "Coeff. of Var.",
        "ko",
        logX=True,
        logY=True,
    )
    title = "Coeff. of Var. abs(#Heads - #Tails)" + numTrialsString
    makePlot(
        xAxis,
        diffsCVs,
        title,
        "Number of Flips",
        "Coeff. of Var.",
        "ko",
        logX=True,
        logY=False,
    )


# start_time = time.time()
# flipPlot2(4, 20, 20)
# print("--- %s seconds ---" % (time.time() - start_time))
# pylab.show()


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads / float(numFlips)


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)


def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + " trials of " + str(numFlips) + " flips each")
    pylab.xlabel("Fraction of Heads")
    pylab.ylabel("Number of Trials")
    pylab.annotate(
        "Mean = " + str(round(mean, 4)) + " \nSD = " + str(round(sd, 4)),
        size="medium",
        xycoords="axes fraction",
        xy=(0.75, 0.5),
    )


def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20, edgecolor="black")
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins=20, edgecolor="black")
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)


# start_time = time.time()
# makePlots(100, 1000, 100000)
# print("--- %s seconds ---" % (time.time() - start_time))
# pylab.show()


from numpy import flip
import scipy.integrate
import pylab
import random


def guassian(x, mu, sigma):
    factor1 = 1.0 / (sigma * ((2 * pylab.pi) ** 0.5))
    factor2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2


def checkEmperical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print("For mu =", mu, "and sigma =", sigma)
        for numStd in (1, 2, 3):
            area = scipy.integrate.quad(
                guassian, mu - numStd * sigma, mu + numStd * sigma, (mu, sigma)
            )[0]
            print(
                "  Fraction within", numStd, "std = ", str(round(area * 100, 2)) + "%"
            )


# checkEmperical(3)


def showErrorBars(minExp, maxExp, numTrials):
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2 ** exp)
        fracHeads, mean, sd = flipSim(2 ** exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, means, yerr=1.96 * pylab.array(sds))
    pylab.semilogx()
    pylab.title("Mean Fraction of Heads (" + str(numTrials) + " trials)")
    pylab.xlabel("Number of flips per trial")
    pylab.ylabel("Fraction of heads & 95% confidence")


# showErrorBars(3, 10, 100)
# pylab.show()