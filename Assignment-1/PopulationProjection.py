# Chapter 1 Question 11
# (Population projection) The US Census Bureau projects population based on the following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years. Assume the current
# population is 312032486 and one year has 365 days.


def __calculate__():
    currentPopulation = 312032486
    newSeconds = 365 * 24 * 60 * 60
    births = newSeconds // 7
    deaths = newSeconds // 13
    immigrant = newSeconds // 45
    newPopulation = births - deaths + immigrant
    print("The Population After 1 Year would be ", currentPopulation + newPopulation)
    newPopulation += newPopulation
    print("The Population After 2 Years would be ", currentPopulation + newPopulation)
    newPopulation += newPopulation
    print("The Population After 3 Year would be ", currentPopulation + newPopulation)
    newPopulation += newPopulation
    print("The Population After 4 Year would be ", currentPopulation + newPopulation)
    newPopulation += newPopulation
    print("The Population After 5 Year would be ", currentPopulation + newPopulation)


__calculate__()
