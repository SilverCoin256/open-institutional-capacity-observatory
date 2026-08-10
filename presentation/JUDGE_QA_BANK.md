# Hard Question Bank With Answer Scaffolds

Practice material only. These are answer scaffolds, not scripts to memorize. Each answer should begin with the direct fact, then the limitation, then the next test.

## Question and significance

1. **What is your exact question?** Can a public workload snapshot support a reproducible descriptive measure of backlog pressure?
2. **Why this question?** Public traces are abundant, but their data-to-claim path is often not reproducible.
3. **What is the one-sentence answer?** In the frozen EOIR window, pending workload grew relative to recorded completions, and the full calculation is auditable.
4. **Why does anyone care?** A lab can inspect and reuse the pipeline without rebuilding provenance and validation scaffolding.
5. **What problem did you personally solve?** I integrated source snapshots, transformations, metrics, outputs, tests, and limitations into one reproducible artifact.
6. **What would be useless about the project?** If the package saves no time or cannot survive an outside reproduction, its infrastructure claim is weak.
7. **What is the unit of analysis?** An institution-period observation, not a person, judge, case, or agency employee.
8. **What is your hypothesis?** Pending workload would grow relative to recorded completions in the selected window.
9. **Was the question decided before seeing the data?** The final audit narrows the claim to the frozen series and explicitly reports what is descriptive.
10. **What is the strongest alternative question?** Whether an independently measured capacity variable predicts backlog dynamics across institutions.

## Data and provenance

11. **Where did the data come from?** The released source register identifies agency sources, URLs, checksums, terms notes, and inheritance caveats.
12. **Did you collect the data yourself?** I assembled and froze the snapshot; the source rows are agency-originated or inherited, not newly audited live data.
13. **Can someone re-download the exact source?** Not yet with complete provenance; that is a documented limitation and next validation task.
14. **Why freeze data instead of using a live API?** A frozen snapshot makes a release reproducible even when an agency revises a page.
15. **How do you know the source was not altered?** The repository records SHA-256 checksums for the frozen files.
16. **What does a checksum prove?** It proves artifact identity after capture, not that the original source was correct.
17. **Why is retrieval provenance incomplete?** The snapshot was inherited from prior research and its original retrieval timestamp cannot be recovered.
18. **What is the biggest data risk?** Definition changes or an unrecoverable source lineage could make adjacent values incomparable.
19. **What did you do about that risk?** I restricted the authoritative result and state the provenance gap instead of hiding it.
20. **Are the later rows complete?** FY2026 is not complete as of the audit date; later rows are excluded from the main inference.

## Measurement

21. **Define QAI.** QAI equals current pending minus prior pending, divided by current completions.
22. **Why call it acceleration?** The name is inherited project terminology; the safe interpretation is normalized backlog change.
23. **Is QAI mathematically novel?** No. I do not claim that it is.
24. **Why keep a familiar ratio?** A named implementation convention can make a reproducible workflow inspectable, if its limits are explicit.
25. **What does positive QAI mean?** Pending increased relative to current completions in that transition.
26. **What does negative QAI mean?** Pending declined relative to current completions; it does not prove resolution or improved quality.
27. **What if completions are zero?** QAI is undefined, not zero.
28. **What if pending definitions change?** The adjacent comparison becomes invalid or requires a documented break adjustment.
29. **Why not use clearance rate?** Clearance rate answers a related question; OICO preserves QAI as a transparent normalized backlog-change signal and compares alternatives.
30. **Which alternative was strongest?** The direction persisted under raw change, prior-pending, average-pending, and current-plus-prior-completions normalization.

## Empirical result

31. **What is the headline number?** Pending rose from 826,488 to 3,925,351 between FY2016 and FY2024.
32. **How much is that?** A 4.749435-fold increase in the frozen snapshot.
33. **How many positive transitions?** Eight of eight in FY2017-FY2024.
34. **What was the peak QAI?** 1.579835 in FY2024.
35. **How many observations?** Nine periods and eight comparable transitions in the authoritative window.
36. **Is eight observations enough for a general theory?** No; it is enough for a bounded descriptive case.
37. **Did you calculate uncertainty intervals?** No meaningful asymptotic interval is claimed for this tiny aggregate series.
38. **What happens if one transition is removed?** The mean remains positive; the check is sensitivity, not inferential proof.
39. **Could one year drive the result?** No single authoritative transition is required for the positive sign pattern, but the sample is still small.
40. **Could reporting changes drive it?** Yes; that is one of the principal alternative explanations.

## Causality and interpretation

41. **Did capacity decline?** The data do not identify capacity directly.
42. **Did staffing fail?** No staffing variable or causal design is present.
43. **Did policy cause the backlog?** The case cannot answer that.
44. **Did AI cause the backlog?** No AI exposure or intervention is identified.
45. **Did oversight fail?** No; a backlog proxy is not oversight quality.
46. **Can this rank institutions?** Not responsibly in v1; definitions and denominators are not commensurate.
47. **Can it rank judges or workers?** No; the data are aggregate and the use would be ethically and scientifically inappropriate.
48. **Does a negative value mean success?** No; it can reflect reporting, composition, prioritization, or other changes.
49. **What is the causal claim?** There is none.
50. **What is the most likely misuse?** Converting an observable queue statistic into a moral or managerial judgment about an institution.

## Software and reproducibility

51. **What did you actually build?** A Python package, CLI, data layout, validation path, notebooks, benchmark pilots, figures, and public documentation.
52. **What are the runtime dependencies?** The package has no runtime dependencies and requires Python 3.10 or newer.
53. **How does reproduction start?** Install the package, run the documented reproduction command, and inspect the report and checksums.
54. **What does CI test?** The package, data validation, notebooks, release path, and multiple supported Python versions.
55. **Why include notebooks?** They expose the analysis to researchers and students who may not begin with the CLI.
56. **Why include checksums?** To detect unintended artifact drift between the release and a reproduction.
57. **What is a clean-room audit?** A test from a built source distribution rather than the author's working tree.
58. **Can an outsider reproduce without credentials?** Yes, the public release route requires no private credential.
59. **What is your test coverage?** 91% overall and 95% for QAI in the current audit.
60. **Does coverage prove scientific validity?** No; it tests implementation paths, not construct validity.

## Benchmark design

61. **Is OICO a benchmark?** It contains benchmark pilots, not a validated community benchmark.
62. **Why no leaderboard?** Labels are small, proxy-based, or synthetic and lack independent ground truth.
63. **What is the queue forecast baseline?** Persistence of the previous QAI value.
64. **What is the saturation baseline?** A threshold against an institution-specific proxy label.
65. **What is wrong with proxy labels?** They can reward agreement with the author's construction rather than real-world accuracy.
66. **What is wrong with synthetic scenarios?** They demonstrate assumptions but are not calibrated institutional evidence.
67. **What would make a real benchmark?** Multiple sources, frozen splits, independent labels, leakage controls, baselines, and external validation.
68. **Why include weak pilots?** They are useful for software regression and teaching if clearly demoted.
69. **Could a model win by exploiting artifacts?** Yes; leakage and proxy-label overfitting are explicit risks.
70. **What benchmark task comes next?** Predict or explain workload dynamics against an independently recovered panel and pre-specified outcomes.

## AI governance and ethics

71. **What does OICO measure about AI?** V1 contains accountability-language coding and scenario modules; neither carries the EOIR flagship claim.
72. **Does ASI measure accountability?** It measures specificity of accountability language in a small coded corpus.
73. **Does language predict implementation?** Not in the current evidence.
74. **Why retain ASI?** It is a transparent beta codebook and reproducibility asset for future validation.
75. **Could AI-generated text bias the project?** Yes; the repository records AI use and requires human verification and attribution.
76. **Did AI write the research?** The project materials disclose AI assistance; scientific responsibility and final wording remain the author's.
77. **Could the data identify people?** The flagship is aggregate; new sensitive sources require a separate privacy review.
78. **Could a public agency misuse this?** Yes, especially for punitive ranking; the documentation prohibits that interpretation.
79. **Should OICO automate decisions?** No. It is an audit and research tool, not an eligibility or personnel system.
80. **What ethical review is next?** Domain-specific review before adding case-level, demographic, or sensitive administrative records.

## Novelty and prior work

81. **What did prior work already show?** EOIR backlog growth and completion pressure are documented by government, GAO, and scholarship.
82. **What is your difference from a spreadsheet?** The difference is the reproducible package contract, not the arithmetic alone.
83. **What is your difference from a data portal?** OICO connects data lineage to metrics, outputs, tests, benchmark caveats, and reuse documentation.
84. **What is your difference from a capacity index?** OICO refuses to equate a workload proxy with latent capacity.
85. **What existing research is the closest warning?** Work on administrative capacity argues that capacity is multidimensional and requires validation.
86. **Why is one agency insufficient?** It does not establish external validity or a general construct.
87. **What is the literature gap?** A reusable, critique-oriented bridge between public workload traces and reproducible software practice may be useful, but adoption is untested.
88. **Are you claiming priority?** No; this audit is a calibration, not a priority claim.
89. **What would make the project genuinely novel?** A validated comparative measure with independent outcomes and transparent uncertainty.
90. **What would disprove your novelty claim?** An existing open package with the same integrated data, provenance, benchmark, and teaching contract that is demonstrably reusable.

## External validation and impact

91. **Who uses OICO today?** No named external lab, professor, course, paper, or conference artifact is verified.
92. **How many independent reproductions?** Zero.
93. **How many citations?** Zero published citations verified.
94. **How many forks or downloads?** Repository activity is not used as adoption evidence unless independently attributable and substantively used.
95. **Why not count internal CI?** It is author-controlled infrastructure.
96. **Why not create a professor endorsement?** That would be fabricated without a real attributable recommendation.
97. **What is the first external milestone?** One independent reproduction with a public or auditable report.
98. **What is the second milestone?** Substantive external methodological feedback or an external contribution.
99. **What would count as adoption?** A lab, course, paper, or conference artifact that names and uses OICO in an attributable record.
100. **What is the final impact claim today?** The project is publicly available and ready to invite validation; measurable external adoption has not yet occurred.

## Personal ownership and future work

101. **Which part is yours?** The design decisions, integration, testing, documentation, interpretation, and bounded scientific claims are attributable to the project author.
102. **What is the hardest implementation decision?** Separating stable, beta, and experimental evidence states.
103. **What did you remove?** Causal language, unvalidated leaderboard claims, later-row inference, and unearned adoption claims.
104. **What did you learn?** A reproducible package can be technically strong while its central statistic remains scientifically ordinary.
105. **What would you do first with a year?** Rebuild the source panel with recoverable provenance and preregister the construct validation.
106. **What would you not do?** Add more modules merely to make the repository look larger.
107. **What is the most important future variable?** An independently measured capacity or outcome variable linked to the workload series.
108. **What is the main maintenance risk?** A single maintainer and changing agency definitions.
109. **What would make you retire the project?** A material source error, irreconcilable provenance, or failure of independent replication.
110. **What is your closing sentence?** OICO is a careful instrument for asking what public traces can support, and its next test must come from someone other than its author.
