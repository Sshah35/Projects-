(define (problem RotimaticProblem)
	(:domain RotiDoman)
	(:objects m)
	(:init
        (NeedsWaterCup m)
        (NeedsFlourContainer m)
        (NeedsEmptyMachine m)
        (NeedsOffSwitch m)
	)
	(:goal (and
        (HasCookedRoti m))
	)
)