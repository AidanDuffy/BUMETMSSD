from money_model import MoneyModel
import matplotlib.pyplot as plt

def main():
    """model = MoneyModel(10)
    for i in range(10):
        model.step()
    wealth = [agent.wealth for agent in model.schedule.agents]
    plt.hist(wealth)
    plt.show()"""

    wealth = []
    for j in range(100):
        model = MoneyModel(10, 50)
        for i in range(10):
            model.step()
        for agent in model.schedule.agents:
            wealth.append(agent.wealth)
    plt.hist(wealth)
    plt.show()

if __name__ == '__main__':
    main()