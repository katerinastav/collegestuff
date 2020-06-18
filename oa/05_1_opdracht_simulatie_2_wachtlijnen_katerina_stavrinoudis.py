import ciw
N = ciw.create_network(
	arrival_distributions={'Class 0':[ciw.dists.Exponential(20.0),
	ciw.dists.NoArrivals()],
	'Class 1': [ciw.dists.NoArrivals(),
	ciw.dists.Exponential(5.0)]},
	service_distributions={'Class 0': [ciw.dists.Exponential(24.0),
	ciw.dists.Deterministic(0.0)],
	'Class 1': [ciw.dists.Deterministic(0.0),
	ciw.dists.Exponential(6.0)]},
	routing={'Class 0': [[0.0, 0.0],
                             [0.0, 0.0]],
'Class 1': [[0.0, 0.0],
            [0.0, 0.0]]},
number_of_servers=[1, 1],
)
average_waits_1 = []
average_waits_2 = []
for trial in range(10):
	ciw.seed(trial)
	Q = ciw.Simulation(N)
	Q.simulate_until_max_time(14)
	recs = Q.get_all_records()
	waits1=[r.waiting_time for r in recs if r.node==1 and r.arrival_date > 3 and r.arrival_date < 11]
	waits2=[r.waiting_time for r in recs if r.node==2 and r.arrival_date > 3 and r.arrival_date < 11]
	average_waits_1.append(sum(waits1) / len(waits1))
	average_waits_2.append(sum(waits2) / len(waits2))

print(sum(average_waits_1) / len(average_waits_1))

print(sum(average_waits_2) / len(average_waits_2))

