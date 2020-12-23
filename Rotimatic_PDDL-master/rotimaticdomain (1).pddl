(define (domain RotiDoman)
    (:predicates
	(NeedsWaterCup ?x)
	(NeedsFlourContainer ?x)
	(NeedsEmptyMachine ?x)
	(NeedOnSwitch ?x)
	(FilledWaterCup ?x)
	(FilledFlourContainer ?x)
	(HasEmptyMachine ?x)
	(HasLoadedMachine ?x)
	(HasOnSwitch ?x)
	(HasCookedRoti ?x)
    )
    (:action FillWaterCup
	:parameters (?x)
	:precondition (and (NeedsWaterCup ?x))
	:effect (and
		(not (NeedsWaterCup ?x))
		(FilledWaterCup ?x) )
    )
    (:action FillFlourContainer
	:parameters (?x)
	:precondition (and (NeedsFlourContainer ?x))
	:effect (and
		(not (NeedsFlourContainer ?x))
		(FilledFlourContainer ?x) )
    )
    (:action LoadEmptyMachine
	:parameters (?x)
	:precondition (and(NeedsEmptyMachine ?x))
	:effect (and
		(not (NeedsEmptyMachine ?x))
		(HasEmptyMachine ?x) )
    )
    
    (:action OnTheSwitch
	:parameters (?x)
	:precondition (and (NeedOnSwitch ?x))
	:effect (and
		(not (NeedOnSwitch ?x))
		(HasOnSwitch ?x) )
    )
    
    (:action MakeRoti
	:parameters (?x)
	:precondition (and
			(FilledWaterCup ?x)
			(FilledFlourContainer ?x)
			(HasEmptyMachine ?x)
			(HasOnSwitch ?x))	
	:effect (and
		(not (HasEmptyMachine ?x))
		(HasLoadedMachine ?x)
		
		(not (HasOnSwitch ?x))
		(NeedOnSwitch ?x)
		(not (FilledWaterCup ?x))
		(NeedsWaterCup ?x)
		(not (FilledFlourContainer ?x)) 
		(NeedsFlourContainer ?x))
		
    )

    (:action CookedRoti
	:parameters (?x)
	:precondition (and
		(HasLoadedMachine ?x) )
	:effect (and
		(not (HasLoadedMachine ?x))
		(HasCookedRoti ?x))
    )
)