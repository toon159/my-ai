from jmetal.algorithm import NSGAII
from jmetal.operator import Polynomial, SBX, BinaryTournamentSelection
from jmetal.component import RankingAndCrowdingDistanceComparator, BasicAlgorithmObserver

from jmetal.problem import ZDT1
problem=ZDT1()
algorithm = NSGAII(
   problem=ZDT1(),
   population_size=100,
   max_evaluations=25000,
   mutation=Polynomial(probability=1.0/problem.number_of_variables, distribution_index=20),
   crossover=SBX(probability=1.0, distribution_index=20),
   selection=BinaryTournamentSelection(comparator=RankingAndCrowdingDistanceComparator())
)

algorithm.run()
front = algorithm.get_result()
basic = BasicAlgorithmObserver(frequency=1.0)
algorithm.observable.register(observer=basic)
