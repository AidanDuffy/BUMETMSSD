from mesa import Agent, Model
from mesa.time import *


class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, proportion):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.proportion = proportion/100


    def step(self):
        if self.wealth == 0:
            return
        elif self.wealth < 1:
            prop = self.proportion/2
        elif self.wealth > 2:
            prop = self.proportion*2
        else:
            prop = self.proportion
        other_agent = self.random.choice(self.model.schedule.agents)
        proportion_of_wealth = self.wealth*self.random.randint(0,100)/100
        other_agent.wealth += proportion_of_wealth
        self.wealth -= proportion_of_wealth
        print ("Hi, I am agent " + str(self.unique_id) +". My wealth is " +
               str(self.wealth))


class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, proportion):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            agent = MoneyAgent(i, self, proportion)
            self.schedule.add(agent)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()