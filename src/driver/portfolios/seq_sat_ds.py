# -*- coding: utf-8 -*-

OPTIMAL = False

CONFIGS = [
    # fork-decoupled search with fancy pruning
    (100, ["--decoupling",
           "fork(search_type=sat, pruning=cost_frontier(irrelevance=TRANSITIONS), max_leaf_size=1000000)",
           "--heuristic",
           "hff=ff(cost_type=H_COST_TYPE)",
           "--search",
           "lazy_greedy(hff, preferred=hff, cost_type=S_COST_TYPE, bound=BOUND)"]),
    # decoupled search
    (1000, ["--decoupling",
           "portfolio(fallback_on_abstain=false, overwrite_options=true, choose_max_leaves=true,"
           "          factorings=[fork(search_type=sat, max_leaf_size=1000000), ifork(search_type=sat, max_leaf_size=1000000), incarcs(search_type=sat, max_leaf_size=100000)])",
           "--heuristic",
           "hff=ff(cost_type=H_COST_TYPE)",
           "--search",
           "lazy_greedy(hff, preferred=hff, cost_type=S_COST_TYPE, bound=BOUND, symmetry=symmetry_state_pruning(lex_prices=false, lex_num_states=false, lex_goal_cost=false))"]),
    # lama first iteration + symmetries
    (690, ["--heuristic",
           "hlm1,hff1=lm_ff_syn(lm_rhw(reasonable_orders=true,"
           "                           lm_cost_type=H_COST_TYPE,cost_type=H_COST_TYPE))",
           "--search", 
           "lazy_greedy([hff1,hlm1],preferred=[hff1,hlm1], cost_type=S_COST_TYPE, reopen_closed=false, symmetry=symmetry_state_pruning, bound=BOUND)"]),
    # lama first iteration => backup in case of conditional effects
    (10, ["--heuristic",
           "hlm1,hff1=lm_ff_syn(lm_rhw(reasonable_orders=true,"
           "                           lm_cost_type=H_COST_TYPE,cost_type=H_COST_TYPE))",
           "--search", 
           "lazy_greedy([hff1,hlm1],preferred=[hff1,hlm1], cost_type=S_COST_TYPE, reopen_closed=false, bound=BOUND)"])

     ]

# ff_lm_eager_wastar
FINAL_CONFIG = [
    "--heuristic",
    "hlm,hff=lm_ff_syn(lm_rhw(reasonable_orders=true,"
    "                         lm_cost_type=H_COST_TYPE,cost_type=H_COST_TYPE))",
    "--search", """iterated([
                     lazy_greedy([hff,hlm],preferred=[hff,hlm],
                                 cost_type=one,reopen_closed=false, bound=BOUND),
                     lazy_greedy([hff,hlm],preferred=[hff,hlm],
                                 reopen_closed=false, bound=BOUND),
                     lazy_wastar([hff,hlm],preferred=[hff,hlm],w=5, bound=BOUND),
                     lazy_wastar([hff,hlm],preferred=[hff,hlm],w=3, bound=BOUND),
                     lazy_wastar([hff,hlm],preferred=[hff,hlm],w=2, bound=BOUND),
                     lazy_wastar([hff,hlm],preferred=[hff,hlm],w=1, bound=BOUND)
                     ],repeat_last=true,continue_on_fail=true)"""                     
]

MEMORY = 7850000000 # close to 8Gb
