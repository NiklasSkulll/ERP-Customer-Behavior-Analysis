<div align="center">

# Literature overview

[![APA 7](https://img.shields.io/badge/APA%207-Citation%20Style-%23352898?style=flat&labelColor=%2315934E)](https://doi.org/10.1037/0000165-000)
[![BibTeX file](https://img.shields.io/badge/Bibliography.bib-BibTeX%20File-%23352898?style=flat&labelColor=%2315934E)](docs/literature/Bibliography.bib)
[![Source Files](https://img.shields.io/badge/docs/literature-Source%20Files-%23352898?style=flat&labelColor=%2315934E)](docs/literature)

</div>

## Table of Contents

- [bibtex-Title: GattermannItschert2022ProactiveCustomerRetention](#bibtex-title-gattermannitschert2022proactivecustomerretention)
- [bibtex-Title: Truong2020SelectiveReviewChangePointDetection](#bibtex-title-truong2020selectivereviewchangepointdetection)
- [bibtex-Title: Abbasimehr2022AnalyticalFrameworkDynamicSegmentation](#bibtex-title-abbasimehr2022analyticalframeworkdynamicsegmentation)
- [bibtex-Title: Wang2024DynamicCustomerSegmentation](#bibtex-title-wang2024dynamiccustomersegmentation)
- [bibtex-Title: Mirkovic2022CustomerChurnPrediction](#bibtex-title-mirkovic2022customerchurnprediction)
- [bibtex-Title: MarinDiaz2022XAIChurnPrediction](#bibtex-title-marindiaz2022xaichurnprediction)
- [bibtex-Title: Civitarese2026XBCDBehavioralChangeDetection](#bibtex-title-civitarese2026xbcdbehavioralchangedetection)
- [bibtex-Title: Adams2007BayesianOnlineChangepointDetection](#bibtex-title-adams2007bayesianonlinechangepointdetection)
- [bibtex-Title: Killick2012OptimalChangepointDetection](#bibtex-title-killick2012optimalchangepointdetection)
- [bibtex-Title: Truong2018RupturesChangePointDetection](#bibtex-title-truong2018ruptureschangepointdetection)

---

## bibtex-Title: GattermannItschert2022ProactiveCustomerRetention

**Title: `Proactive customer retention management in a non-contractual B2B setting based on churn prediction with random forests`**

**Summary:**
- **Topic:** Machine-learning-based prediction of partial customer churn and proactive retention management in a non-contractual B2B wholesale setting.
- **Goal:** Develop and validate a B2B churn prediction model, identify influential predictors, and test in a field experiment whether prediction-based targeting reduces churn and improves revenue development.
- **Method:** Logistic regression, linear support vector machines, and a weighted random forest with balanced class weights were tuned through grid search with 5-fold cross-validation; the best-performing model was selected using out-of-period evaluation and multiple monthly training time slices.
- **Data and unit of analysis:** Customer master data, invoicing transactions, CRM activity logs, and delivery-performance data from a large European convenience wholesaler; approximately 5,000 independent B2B customers were analyzed at customer level. Features used the preceding 12 months, while churn labels covered the subsequent three months.
- **Features or variables:** Recency, order frequency, monthly and quarterly revenue levels and variability, recent revenue development, segment-level revenue and order frequency, customer and company margins, delivery issues, product value not delivered, on-time in-full performance, number and recency of contacts with field representatives and phone agents, number of product segments ordered, returns, relationship length, contract conditions, store type, payment method, region, and assigned warehouse.
- **Detection or classification approach:** Binary prediction of future partial churn. A customer was labeled a churner when, over three months, revenue declined by at least 50% in at least one product segment and total revenue declined by at least 30% relative to the previous three months.
- **Explainability approach:** SHAP was used for global feature importance and local explanation of individual predictions. Summary plots ranked influential variables, while force plots showed which feature values increased or decreased a specific customer’s predicted churn probability.
- **Evaluation:** Historical out-of-period testing used AUC, average precision, top-decile lift, precision, recall, true-positive rate, and false-positive rate. A randomized field experiment with 4,920 customers compared ML-based selection with random selection while holding the contacted proportion constant.
- **Key finding:** The random forest outperformed logistic regression and linear SVM, achieving AUC 0.758, average precision 0.331, and top-decile lift 3.625 on the reported test set; the respective random baseline values were 0.500, 0.099, and 1.000.
- **Key finding:** In the field experiment, ML-based targeting reduced the full-group churn rate from 12.93% to 11.55%. Controlling for predicted churn probability, customers in the ML treatment were reported as 15% less likely to churn, and their three-month revenue-change ratio was 4.2 percentage points higher.
- **Conclusion:** Prediction-based retention activities can reduce churn and improve short-term revenue development in a non-contractual B2B wholesale context, even with only a few thousand customers and existing phone-agent and field-representative processes.
- **Relevance classification:** Conceptually relevant.
- **Relevance to my research question:** The paper supports the use of longitudinal ERP-like transaction and CRM data to characterize customer behavior through revenue, order-frequency, product-segment, margin, and relationship variables. Its SHAP analysis is transferable to explain which dimensions drive a customer-level alert, but the study predicts a predefined churn outcome rather than detecting and typing arbitrary behavioral change points.
- **Limitation:** The study is based on a one-time experiment at one wholesale company. The authors also note unresolved issues around repeated retraining after customers have received retention treatments, limited data for uplift modeling, and uncertain generalizability to other B2B relationships.
- **Important distinction:** The paper studies supervised binary partial-churn prediction and intervention targeting. It does not perform Change Point Detection, derive a taxonomy of purchase-behavior change types, or classify multiple kinds of historical behavior change.

---

## bibtex-Title: Truong2020SelectiveReviewChangePointDetection

**Title: `Selective review of offline change point detection methods`**

**Summary:**
- **Topic:** Selective review of offline methods for detecting multiple change points in univariate and multivariate time series.
- **Goal:** Organize the change point detection literature into a practical framework that helps practitioners select and combine methods for a given retrospective segmentation task.
- **Method:** The review characterizes each detection procedure through three components: a cost function defining segment homogeneity, a search method solving the segmentation problem, and a constraint or penalty controlling the number of detected changes.
- **Detection or classification approach:** The paper formulates offline Change Point Detection as selecting a segmentation that minimizes the sum of segment costs, either for a known number of changes or with an added complexity penalty when the number is unknown.
- **Features or variables:** The reviewed cost functions can detect changes in means, variances and covariance structures, probability distributions, regression coefficients, autoregressive coefficients, Poisson rates, ranks, and kernel mean embeddings; the framework supports multivariate observations in (\mathbb{R}^d).
- **Detection or classification approach:** Exact search methods include dynamic programming for a fixed number of changes and PELT for an unknown number under a linear penalty. Approximate methods include sliding windows, Binary Segmentation, Wild Binary Segmentation, Circular Binary Segmentation, and Bottom-Up Segmentation.
- **Detection or classification approach:** Parametric costs include (c_{L2}), Gaussian mean-and-scale costs, Poisson likelihood, piecewise linear regression, autoregressive models, and Mahalanobis-type metrics; non-parametric alternatives include empirical-distribution, rank-based, and kernel-based costs.
- **Explainability approach:** Not clearly stated in the paper. The methods identify temporal boundaries and homogeneous regimes, but the review does not provide a dedicated feature-contribution or local explanation method for why a particular multivariate change was detected.
- **Evaluation:** The review describes asymptotic consistency and empirical metrics including annotation error, Hausdorff distance, Rand index, precision, recall, and F1-score with a user-defined tolerance around true change points.
- **Key finding:** The choice of cost function determines the type of change that can be detected, while the search method mainly governs the trade-off between computational complexity and segmentation accuracy.
- **Key finding:** PELT provides an exact solution for linearly penalized segmentation and may achieve approximately linear complexity under stated assumptions; sliding-window and Bottom-Up methods are also linear in signal length, while Binary Segmentation has approximately (O(T\log T)) complexity and fixed-(K) dynamic programming has (O(KT^2)) complexity.
- **Conclusion:** A modular combination of cost function, search method, and constraint enables practitioners to design an offline Change Point Detection procedure suited to a specific signal model, type of change, computational budget, and knowledge of the number of changes.
- **Relevance classification:** Methodologically relevant.
- **Relevance to my research question:** The paper provides a direct methodological foundation for segmenting multivariate customer-level ERP time series into behaviorally homogeneous periods. Its cost-function framework can be mapped to changes in revenue means, variability, product-category distributions, or multivariate customer profiles, while PELT and sliding-window methods are especially relevant candidate approaches for detecting behavioral transitions.
- **Limitation:** The review excludes Bayesian Change Point Detection methods and focuses on offline retrospective segmentation; it also assumes piecewise-stationary signals and does not address domain-specific change typologies, customer behavior interpretation, or causal explanations.

---

## bibtex-Title: Abbasimehr2022AnalyticalFrameworkDynamicSegmentation

**Title: `An analytical framework based on the recency, frequency, and monetary model and time series clustering techniques for dynamic segmentation`**

**Summary:**
- **Topic:** Dynamic B2B customer segmentation by representing transaction behavior as RFM time series and clustering customers with similar temporal patterns.
- **Goal:** Overcome the limitations of static customer segmentation by preserving the temporal order of transactions, identifying homogeneous behavioral groups, and interpreting each segment’s dominant trends for CRM decision support.
- **Method:** The framework aggregates time-stamped transactions into periodic RFM series, computes pairwise time-series distances, applies hierarchical, spectral, and k-shape clustering, selects the best model using internal cluster-validity indices, and analyzes cluster centroid series.
- **Data and unit of analysis:** Eleven consecutive months of POS transaction data from a bank, comprising 2,156,394 purchases. The customers are grocery and appliance merchants, treated as B2B customers of the bank; transactions were aggregated into weekly bins.
- **Features or variables:** Recency, Frequency, and Monetary value are defined for each time interval. In the empirical study, Recency was removed because every selected customer transacted every day, and Monetary value was used as the behavioral representation because transaction count did not necessarily imply high value.
- **Detection or classification approach:** Customer-level Monetary time series were clustered using hierarchical clustering, normalized spectral clustering, and k-shape. The evaluated distance measures were Dynamic Time Warping, Complexity-Invariant Distance, temporal correlation coefficient, and Shape-Based Distance; solutions with four, five, and six clusters were compared.
- **Explainability approach:** Descriptive interpretation through cluster centroid time series, fitted trend lines, manually assigned segment labels, and analysis of seasonality and trend direction. The study does not provide local feature-contribution explanations for individual customers.
- **Evaluation:** Because no true cluster labels were available, the authors used the silhouette and Caliński–Harabasz internal validity indices to compare clustering-method and distance-measure combinations.
- **Key finding:** For grocery retailers, the best four-cluster solution was hierarchical clustering with Complexity-Invariant Distance, with silhouette 0.39 and Caliński–Harabasz 3641.14. For appliance retailers, spectral clustering with Complexity-Invariant Distance performed best, with silhouette 0.46 and Caliński–Harabasz 5696.5.
- **Key finding:** Both retailer groups were divided into High-Value, Middle-Value, Middle-to-Low-Value, and Low-Value segments. The centroid series revealed temporal patterns including growth, decline, relative stability, and recurring seasonality.
- **Conclusion:** Modeling customer transactions as time series can expose dynamic behavioral patterns that fixed-period aggregation may conceal, while the choice of time-series distance measure—particularly Complexity-Invariant Distance in this case—substantially affects segmentation quality.
- **Relevance classification:** Directly relevant.
- **Relevance to my research question:** The paper directly supports customer-level aggregation of transactional data into weekly behavioral time series and the use of temporal clustering to derive interpretable B2B behavior groups. Its centroid and trend analysis is relevant for defining change vectors and interpretable customer states, although it clusters complete trajectories rather than detecting specific change points or assigning individual detected transitions to a formal change-type taxonomy.
- **Limitation:** The empirical analysis uses only transaction data and lacks contextual variables such as location, store size, and staff count. The observation period is limited to eleven months, which the authors state restricts deeper behavioral analysis.
- **Important distinction:** The paper performs dynamic segmentation of complete customer time series, not Change Point Detection. Its labels describe overall value-based trajectory groups rather than discrete customer-level behavior changes such as revenue decline, assortment narrowing, or margin deterioration.

---

## bibtex-Title: Wang2024DynamicCustomerSegmentation

**Title: `A dynamic customer segmentation approach by combining LRFMS and multivariate time series clustering`**

**Summary:**
- **Topic:** Dynamic segmentation of automotive-parts customers using multivariate customer-level time series and an extended LRFMS value model.
- **Goal:** Improve dynamic customer segmentation by addressing the randomness of the traditional Recency indicator, incorporating customer satisfaction, and clustering several behavioral dimensions jointly rather than relying on univariate time series.
- **Method:** The proposed DCSLM framework converts transactions into Length, modified Recency, Frequency, Monetary, and Satisfaction time series, computes feature weights, constructs fuzzy membership matrices from multivariate and dimension-specific distances, and applies spectral clustering, affinity propagation, and k-medoids.
- **Data and unit of analysis:** Approximately 300,000 transaction records from automotive-parts agents on a Chinese ASP/SaaS manufacturing value-chain platform, covering 2019–2021. Three product datasets were created for different parts categories, with customer behavior aggregated into two-week intervals.
- **Features or variables:** Length between first and last transaction in an interval; average modified Recency based on the last (p) transactions; transaction Frequency; accumulated Monetary value; and Satisfaction derived from product quality, delivery timeliness, and after-sales service ratings with equal weights in the empirical study.
- **Detection or classification approach:** Customers are clustered on complete multivariate LRFMS trajectories. DTW-D captures overall multivariate alignment, while composite measures combine DTW-D with dimension-level CID or SBD; Density Peaks Clustering is used to identify cluster centers before fuzzy membership construction.
- **Explainability approach:** Clusters are interpreted descriptively through representative centroid series, moving-average trend lines, mean Monetary levels, manually assigned segment labels, and associated marketing implications. The method does not provide local feature-attribution explanations for individual customer changes.
- **Evaluation:** Competing solutions with three, four, or five clusters were assessed using the silhouette index; broader comparisons used silhouette, Dunn Index, and Davies–Bouldin Index against an RFM variant and several multivariate clustering and customer-segmentation baselines.
- **Key finding:** The selected configurations achieved silhouette values of 0.7506 for PD1 with spectral clustering and DTW-D+SBD, 0.9313 for PD2 with the paper’s reported best DTW-D+CID configuration, and 0.8804 for PD3 with DTW-D+SBD and five clusters.
- **Key finding:** Compared with the RFM-based DCSRM variant, DCSLM increased silhouette by 18.7283%, 14.6780%, and 21.6190% and Dunn Index by 35.66%, 28.56%, and 33.22% across PD1, PD2, and PD3, while also producing lower Davies–Bouldin values.
- **Conclusion:** Combining LRFMS with multivariate time-series clustering provides a more detailed representation of customer value and yields stronger internal clustering results than the traditional RFM-based alternative in the examined automotive-parts datasets.
- **Relevance classification:** Directly relevant.
- **Relevance to my research question:** The study directly demonstrates multivariate, customer-level temporal profiling from transaction data and derives interpretable customer groups from changes in frequency, monetary value, relationship duration, recency, and satisfaction. Its composite-distance and feature-weighting ideas are transferable to ERP-derived change vectors, although the study segments entire trajectories rather than detecting discrete change points or classifying individual change events.
- **Limitation:** The method has quadratic-order components and becomes slower as customer volume grows, potentially limiting timely reflection of recent changes. The analysis also relies mainly on transaction data and lacks variables such as location, reputation, and browsing history.
- **Important distinction:** The paper performs dynamic multivariate customer segmentation and trend interpretation, not Change Point Detection. Its labels—such as important retention, secondary important retention, development, loyal, and general customers—describe overall segment membership rather than a formal taxonomy of detected behavioral changes.

---

## bibtex-Title: Mirkovic2022CustomerChurnPrediction

**Title: `Customer Churn Prediction in B2B Non-Contractual Business Settings Using Invoice Data`**

**Summary:**
- **Topic:** Binary customer churn prediction in a non-contractual B2B setting using only invoice-level transaction data.
- **Goal:** Assess whether invoice data alone can support reliable churn prediction, how different historical feature-window lengths and churn definitions affect performance, and whether multi-slicing outperforms conventional single-slicing.
- **Method:** Logistic Regression with L2 regularization, linear-kernel Support Vector Machines, and Random Forests were trained with nested 10-fold cross-validation and grid-search hyperparameter tuning; models were tested on a more recent out-of-period dataset.
- **Data and unit of analysis:** Invoice data from an Eastern European B2B seller and distributor of agricultural goods and equipment, covering January 2019 to February 2022; 280,502 invoices, 1,962,152 invoice lines, and 3470 customers. Features and churn labels were constructed at customer level using monthly periods.
- **Features or variables:** Cumulative Features and monthly Delta Features derived from invoice date, customer, product, price, and quantity, including recency, invoice frequency, invoiced amounts, inter-purchase times, distinct-product counts, quantities, tenure, per-product statistics, standard deviations, and differences between the latest month and earlier months.
- **Detection or classification approach:** Churn was defined as no purchase during the subsequent one, two, or three months. Multi-slicing generated repeated monthly customer snapshots, while Delta Feature windows of 1, 3, 6, 9, or 12 months explicitly represented changes in purchasing patterns.
- **Explainability approach:** Global permutation-based feature importance was calculated for the best-performing models. The paper provides no local explanation of an individual customer's prediction and identifies explainable machine-learning methods as future work.
- **Evaluation:** A total of 45 multi-slicing models were evaluated using AUC and Top-Decile Lift; classifier differences were tested with one-way ANOVA and Tukey’s HSD, while multi-slicing and single-slicing were compared using two-sample t-tests.
- **Key finding:** Random Forest achieved the highest average performance, with average AUC 0.8925 and average Top-Decile Lift 4.4375. Its best result was obtained for the two-month churn definition with a 12-month Delta Feature window: AUC 0.9050 and Top-Decile Lift 4.9090.
- **Key finding:** Multi-slicing outperformed single-slicing across the tested combinations; average Random Forest performance increased from AUC 0.8715 and Top-Decile Lift 3.9461 to AUC 0.8925 and Top-Decile Lift 4.4375. Differences were statistically significant for AUC, (p=0.001), and Top-Decile Lift, (p<0.001).
- **Conclusion:** Robust churn models can be built from invoice data alone, and longer historical periods generally improved the best-performing Random Forest models. Alternative one-, two-, and three-month inactivity definitions may support differentiated retention strategies.
- **Relevance classification:** Conceptually relevant.
- **Relevance to my research question:** The paper demonstrates how ERP-like invoice transactions can be aggregated into temporal customer profiles and how month-to-month difference features can quantify changes in frequency, monetary value, quantities, product diversity, and recency. However, these changes are used as predictors of future inactivity rather than detected, classified, and explained as distinct purchase-behavior change types.
- **Limitation:** The data come from one company, industry, and geographic region; the study does not test whether results generalize to other domains, does not investigate shorter cumulative-history periods, uses only three established classifiers, and does not provide detailed explainable-machine-learning analyses.
- **Important distinction:** The study predicts binary churn defined through future inactivity. It does not perform Change Point Detection, identify structural breaks in customer time series, derive a taxonomy of behavior-change types, or explain customer-specific historical changes.

---

## bibtex-Title: MarinDiaz2022XAIChurnPrediction

**Title: `XAI for Churn Prediction in B2B Models: A Use Case in an Enterprise Software Company`**

**Summary:**
- **Topic:** Explainable binary churn prediction for B2B software partners using CRM Contact Center interactions rather than purchase transactions.
- **Goal:** Develop a model-independent methodological process for predicting partner abandonment and explaining black-box model decisions through global and local Explainable Artificial Intelligence techniques.
- **Method:** A KDD- and CRISP-DM-based workflow combines RFID customer assessment, preprocessing, model comparison, class balancing, XGBoost prediction, k-means segmentation, and successive XAI analyses.
- **Data and unit of analysis:** CRM ticket data for 200,615 B2B software partners over 2018–2020; 198,493 partners remained and 2122 left, corresponding to a reported churn rate of approximately 1.06%. Each record represents an aggregated partner-level Contact Center profile.
- **Features or variables:** The RFID variables are recency—the days since the latest service request; frequency—the number of distinct service requests; importance—the average ticket importance; and duration—the total duration of all tickets. The target identifies a CRM “Cancellation Request.”
- **Detection or classification approach:** Logistic Regression, Random Forest, Support Vector Machine, K-nearest neighbors, Decision Tree Classifier, Gaussian NB, and XGboost were compared through K-fold cross-validation. XGboost was selected because it achieved the highest mean ROC AUC, 70.40, with mean accuracy of 98.75%.
- **Explainability approach:** The selected XGboost model was analyzed using global Partial Dependence Plots, global/local Individual Conditional Expectation, ELI5 permutation feature importance, local LIME explanations, local SHAP values, and the global/local Skater framework. The study also relates individual explanations to five RFID-based k-means partner clusters.
- **Evaluation:** Models were evaluated with ROC AUC and accuracy. Because the unbalanced XGBoost model classified no churn cases well but achieved zero recall for churn, the authors applied `scale_pos_weight` and SMOTE-Tomek balancing; the resulting test evaluation reported ROC AUC 0.70, overall accuracy 0.76, churn recall 0.57, churn precision 0.03, and churn F1-score 0.05.
- **Key finding:** Global ELI5 importance ranked importance first with weight 0.3610, followed by frequency 0.2542, duration 0.1998, and recency 0.1849; however, the authors caution that the importance variable is strongly concentrated around its mean and therefore regard this ranking as potentially misleading.
- **Key finding:** SHAP and Skater instead ranked frequency and recency as the strongest predictors, followed by duration and importance. The interpreted pattern indicates greater abandonment propensity among recently incorporated partners with low interaction frequency, whereas partners with more Contact Center interactions showed lower predicted abandonment propensity.
- **Conclusion:** The authors conclude that their agnostic XAI workflow can explain black-box churn predictions and that its results align with the RFID clustering: partners with lower recency and frequency ratings were concentrated in higher-risk clusters, while more established and interactive partners had lower abandonment propensity.
- **Relevance classification:** Methodologically relevant.
- **Relevance to my research question:** The paper provides a transferable combination of global feature-effect analysis, local feature-contribution explanations, and interpretable customer clusters. These techniques are relevant for explaining which dimensions contribute to a detected customer-level change, although the analyzed variables concern Contact Center interactions rather than ERP purchase behavior.
- **Limitation:** The target is extremely imbalanced, and the balanced model obtains only 0.03 precision and 0.05 F1-score for churn despite improving churn recall to 0.57. In addition, the importance feature has little variation, which weakens the reliability of some global feature-importance results.
- **Important distinction:** The paper predicts an explicit cancellation request and explains churn classifications; it does not detect change points, compare before-and-after purchasing profiles, identify temporal purchase-behavior changes, or derive a taxonomy of ERP-based behavior-change types.

---

## bibtex-Title: Civitarese2026XBCDBehavioralChangeDetection

**Title: `X-BCD: Explainable Sensor-Based Behavioral Change Detection in Smart Home Environments`**

**Summary:**
- **Topic:** Explainable, unsupervised detection and characterization of longitudinal behavioral changes from multimodal smart-home sensor data.
- **Goal:** Detect when sustained behavioral changes occur, determine how recurring routines reorganize across consecutive periods, and generate clinician-oriented natural-language explanations of those changes.
- **Method:** X-BCD combines interpretable feature encoding, offline multivariate Change Point Detection, density-based clustering within each segment, cross-segment cluster evolution tracking, template-based intermediate descriptions, and an LLM-based explanation module.
- **Data and unit of analysis:** Longitudinal sensor data from 17 people with Mild Cognitive Impairment living in real homes, observed for approximately 12–30 months; eight belonged to a neurodegenerative cohort and nine to a non-neurodegenerative cohort. The unit of analysis is a subject-specific, daily multivariate feature vector for each behavioral dimension.
- **Features or variables:** Knowledge-driven features cover sleep stages, sleep continuity and duration, sleep schedule, steps and elevation, physical-activity intensity, and cooking behavior. Examples include REM/deep/light sleep duration, wake-ups, time in bed, sleep start/end times, steps, distance, elevation, activity intensities, heart rate, cooktop-use duration, event counts, and time-of-day shares.
- **Detection or classification approach:** PELT with an (l_2) residual cost segments each behavioral time series into internally stable periods; the implementation uses `ruptures`, a minimum segment size of 90 days, and penalty (\beta=60). DBSCAN then identifies routines within each segment, and a thresholded bipartite graph compares clusters between a Reference Period and an Observation Period.
- **Explainability approach:** X-BCD defines six interpretable routine-evolution types: stable, drifting, novel, disappeared, split, and merged. Each change is described through cluster centroids, variance, prevalence, and a drift score combining centroid shift, prevalence change, and variance change; MedGemma 27B converts these grounded representations into explanations of global trend, habit dynamics, and potential implications.
- **Evaluation:** Because no ground-truth change annotations were available, the paper does not report change-detection precision, recall, F1, or detection delay. Evaluation instead uses cohort-level comparisons, distributions of change points and change-type mass, sensitivity analysis for (\beta), similarity threshold (\tau_s), and drift threshold (\tau_d), plus a preliminary expert assessment by neurologists.
- **Key finding:** Most routine mass was assigned to stable and drifting patterns, while novel and disappeared routines were less frequent and splits and merges were relatively rare for fine-grained dimensions. When sleep features were combined into a coarser representation, split and merge events became more frequent, showing that representation granularity materially affects the detected change typology.
- **Key finding:** The cohorts showed different descriptive change patterns: sleep-stage and cooking changes remained detectable for the neurodegenerative group even under stronger change-point penalties, while several changes in the non-neurodegenerative group disappeared earlier. The authors present this as hypothesis-generating evidence, not diagnostic validation.
- **Conclusion:** X-BCD provides structured and interpretable descriptions of how routines persist, drift, emerge, disappear, split, or merge over time. The authors argue that sleep-stage and cooking-related changes appear especially informative in their dataset, while emphasizing that the framework is decision support rather than a diagnostic system.
- **Relevance classification:** Directly relevant.
- **Relevance to my research question:** The framework closely matches the thesis structure: customer-period feature vectors could replace sensor-derived daily vectors; PELT could detect purchase-behavior change points; clustering could identify recurring purchasing profiles; and the six routine-evolution types offer a transferable basis for classifying stable, drifting, emerging, disappearing, splitting, or merging purchasing patterns. Its feature-grounded textual explanations also provide a concrete design for explaining which dimensions changed and how.
- **Limitation:** The evaluation uses only 17 subjects, no annotated ground truth, no state-of-the-art baseline comparison, no formal clinical validation, and only a subset of available behavioral dimensions. Hyperparameter tuning is difficult without labels, the method is retrospective rather than online, and residual LLM hallucinations remain possible.
- **Important distinction:** The paper performs actual multivariate temporal behavior-change detection and explicit change-type classification, unlike churn-prediction studies. However, its application domain is health monitoring with sensor data, not ERP transactions or B2B purchasing.

---

## bibtex-Title: Adams2007BayesianOnlineChangepointDetection

**Title: `Bayesian Online Changepoint Detection`**

**Summary:**
- **Topic:** Online Bayesian detection of abrupt changes in the generative parameters of sequential data.
- **Goal:** Derive an exact online inference algorithm for estimating the most recent changepoint and predicting the next observation using only data observed up to the current time.
- **Method:** The approach recursively computes the posterior distribution of the current run length (r_t), defined as the time elapsed since the latest changepoint, through a message-passing algorithm that combines predictive probabilities with a prior hazard function.
- **Data and unit of analysis:** The paper evaluates the method on three univariate sequential datasets: 4050 well-log measurements, daily Dow Jones Industrial Average returns from July 1972 to June 1975, and weekly coal-mine disaster occurrences from 1851 to 1962.
- **Features or variables:** The method operates directly on sequential observations rather than engineered behavioral features. The demonstrations model changes in a Gaussian mean, a Gaussian variance, and a Poisson event rate.
- **Detection or classification approach:** At each new observation, probability mass either advances to (r_t=r_{t-1}+1) or resets to (r_t=0), indicating a possible changepoint. The transition probability is governed by a hazard function derived from the prior distribution over intervals between changepoints.
- **Explainability approach:** The posterior run-length distribution provides a probabilistic indication of when a change may have occurred, and the predictive distribution quantifies uncertainty. The paper does not provide feature-level contribution explanations, semantic change types, or natural-language explanations.
- **Evaluation:** The paper presents qualitative case-study demonstrations and plots of predictive means or volatility together with posterior run-length probabilities. It does not report labeled precision, recall, F1, false-alarm rate, detection delay, or comparative benchmark results.
- **Key finding:** In the well-log example, posterior resets to run length zero aligned visually with abrupt shifts in the signal mean, while predictive uncertainty increased immediately after detected changepoints.
- **Key finding:** The framework was applied without changing its core inference mechanism to Gaussian-mean, Gaussian-variance, and Poisson-rate models, illustrating its modularity across different likelihoods and data types.
- **Conclusion:** The authors present a simple, exact, predictive online Bayesian changepoint algorithm whose model-specific component can be replaced through a modular “pluggable” architecture.
- **Relevance classification:** Methodologically relevant.
- **Relevance to my research question:** BOCPD is directly transferable to customer-level ERP time series for online detection of shifts in revenue, order frequency, assortment breadth, or other purchase-behavior variables. Its run-length posterior can express uncertainty and support early-warning alerts, but additional methods would be required to classify the detected change and explain which purchase dimensions caused it.
- **Limitation:** Exact per-step time and memory complexity grow linearly with the number of observations seen so far; truncating low-probability run-length hypotheses can reduce average complexity but does not remove the linear worst case. The method also assumes independent segment parameters and conditionally i.i.d. observations within each segment.
- **Important distinction:** The paper addresses online probabilistic changepoint detection and forecasting, not customer churn prediction, behavioral change typology, multivariate feature attribution, or causal explanation.

---

## bibtex-Title: Killick2012OptimalChangepointDetection

**Title: `Optimal detection of changepoints with a linear computational cost`**

**Summary:**
- **Topic:** Efficient exact detection of multiple changepoints in long ordered data sequences by minimizing a penalized segment-cost function.
- **Goal:** Introduce an exact changepoint search method whose computational cost is linear in the number of observations under specified conditions, while retaining the globally optimal segmentation for the chosen objective.
- **Method:** The paper develops **Pruned Exact Linear Time (PELT)**, which extends Optimal Partitioning with a pruning rule that removes candidate changepoints that cannot be optimal in later iterations.
- **Data and unit of analysis:** Univariate ordered sequences are analyzed at the observation level. Evaluation uses simulated Normal data with changes in variance, simulated autoregressive data with changes in order and parameters, hourly North Atlantic wave-height data from January 2005 to September 2012, and a financial application in the supplementary material.
- **Features or variables:** Depending on the experiment, PELT detects changes in variance, mean and variance, or autoregressive structure; segment costs are based on negative log-likelihood, cumulative sum of squares, quasi-likelihood, or Minimum Description Length.
- **Detection or classification approach:** PELT minimizes the sum of segment costs plus a penalty for changepoints. It is compared with **Optimal Partitioning**, **Binary Segmentation**, **Segment Neighbourhood**, and, for autoregressive data, the genetic-algorithm implementation **Auto-PARM**.
- **Explainability approach:** No feature-contribution or local explanation method is provided. Interpretation is limited to the estimated changepoint locations, the resulting temporal segments, and the statistical property modeled within each segment.
- **Evaluation:** Simulation studies vary sequence length and number of changepoints and assess computational time, objective-function value, mean squared error of parameter estimates, correctly detected changepoints, and false detections. A detected changepoint is counted as correct when it lies within 10 time points of the true location.
- **Key finding:** When the expected number of changepoints increases linearly with sequence length and the theorem’s assumptions hold, PELT has expected computational cost (O(n)); its worst-case complexity remains (O(n^2)).
- **Key finding:** In simulations, PELT was orders of magnitude faster than alternative exact methods and produced more accurate segmentations than Binary Segmentation, especially as the number and density of changepoints increased.
- **Key finding:** In the wave-height application, PELT detected 17 changepoints compared with 6 from optimal Binary Segmentation and produced a substantially better likelihood-based segmentation of high- and low-volatility periods.
- **Conclusion:** The authors conclude that PELT combines exact optimization with broad applicability and major computational savings over existing exact search procedures; although Binary Segmentation can be faster in practice, PELT offers substantial statistical-accuracy benefits.
- **Relevance classification:** Methodologically relevant.
- **Relevance to my research question:** PELT is directly transferable as an efficient offline method for detecting structural changes in customer-level ERP time series. However, the paper does not address B2B purchasing data, multivariate customer profiles, behavioral change typologies, or explanations of which purchase features caused a detected change.
- **Limitation / Important distinction:** Linear computational cost depends particularly on the number of changepoints increasing linearly with data length; when changepoints increase more slowly, PELT may no longer scale linearly. The paper studies generic statistical changepoint detection rather than customer-behavior classification, churn prediction, or explainable purchase-change analysis.

---

## bibtex-Title: Truong2018RupturesChangePointDetection

**Title: `ruptures: change point detection in Python`**

**Summary:**
- **Topic:** A Python library for offline multiple change point detection and segmentation of univariate or multivariate non-stationary signals.
- **Goal:** Provide non-specialists with a fast, documented, consistent, and modular framework for exploring non-stationary signals and combining change point algorithms with different statistical models.
- **Method:** The paper presents the software architecture and functionality of `ruptures`, organizing change point detection around separate search-method and cost-function components that can be freely combined or extended.
- **Data and unit of analysis:** The library accepts any univariate or multivariate signal represented as a NumPy array. The illustrative example uses a simulated two-dimensional piecewise-stationary signal with 500 observations and four changepoints.
- **Features or variables:** Supported cost functions can detect changes in mean, scale, linear relationships between dimensions, autoregressive coefficients, and more general distributions through kernel-based or Mahalanobis-type non-parametric costs.
- **Detection or classification approach:** Implemented search procedures include dynamic programming, detection with an (l_0) constraint, Binary Segmentation, bottom-up segmentation, and window-based segmentation. Detection can use a known number of changepoints, a cost budget, or a linear penalty when the number is unknown.
- **Explainability approach:** No feature-contribution, SHAP, causal, or local explanation method is described. Results can be interpreted through detected breakpoints, segment boundaries, the selected cost function, and visual inspection using the display module.
- **Evaluation:** The library includes quantitative segmentation metrics and visualization functions, but the paper does not report a systematic benchmark, comparative metric table, or empirical validation across real datasets.
- **Key finding:** The modular design separates optimization algorithms from cost functions, allowing users to compare methods, substitute models, and integrate new contributions through a consistent interface.
- **Key finding:** In the illustrative kernel example, an RBF kernel maps a simulated two-dimensional signal into a Hilbert space, and dynamic programming detects mean shifts in that transformed representation corresponding to changes in the original covariance structure.
- **Conclusion:** The authors present `ruptures` as a comprehensive change point detection library whose consistent interface, documentation, modularity, and compatibility with the Python scientific ecosystem facilitate method comparison and extension.
- **Relevance classification:** Methodologically relevant.
- **Relevance to my research question:** `ruptures` provides a practical implementation framework for applying several offline change point methods to customer-level univariate or multivariate ERP time series. Its interchangeable cost functions could support detecting different statistical forms of purchase-behavior change, while its window-based and penalized methods enable comparison of alternative detection strategies.
- **Limitation:** The paper does not study B2B customers, ERP transactions, purchase-behavior features, behavioral change typologies, detection delay, false-alarm performance, or feature-level explanations.
- **Important distinction:** This is primarily a software-library paper about generic offline signal segmentation, not an empirical study of customer behavior, a classification of change types, or an explainable analysis of why a customer’s purchasing behavior changed.
