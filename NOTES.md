# Notes: Word Embeddings on *The Crisis* and *Opportunity*, 1910–1930

## Corpus

- Downloaded Nov 1, 2026 from the Internet Archive: 242 issues of *The Crisis* (1910–1930), 96 of *Opportunity* (1923–1930). Nothing missing.
- After cleaning:

| Period | Issues | Words |
|---|---|---|
| 1910–1916 | 74 | 1,929,262 |
| 1917–1923 | 96 | 2,470,428 |
| 1924–1930 | 168 | 4,124,734 |
| **Total** | **338** | **8,524,424** |

- 1910–1916 is *Crisis* only; *Opportunity* begins in 1923.
- Advertisements are still in the text.

### Key word counts (1910–16 / 1917–23 / 1924–30)

- segregation: 726 / 274 / 586
- lynching: 695 / 1,156 / 559
- vote: 753 / 632 / 855
- education: 1,248 / 2,007 / 4,404
- migration: 27 / 329 / 352 (too rare in 1910–16 to trust)

## Models

### 1910–1916

- Vocabulary: 10,433 words (min count 10)
- the 8 words closest to *segregation*:
  ordinance            0.795
  ordinances           0.759
  protesting           0.717
  discrimination       0.712
  ghetto               0.711
  invalid              0.704
  involving            0.699
  jim-crow             0.687

### 1917–1923
- Vocabulary: 12,289 words (min count 10 times)
- 8 words closest to *segregation* : 
  ordinances           0.745
  jim-crowism          0.742
  ordinance            0.734
  discrimination       0.722
  lawlessness          0.712
  jim-crow             0.702
  residential          0.700
  unequal              0.688    

### 1924–1930
- Vocabulary: 17,607 words (each appears at least 10 times)
- 8 words closest to *segregation*:
  residential          0.834
  unconstitutional     0.722
  ordinances           0.711
  legality             0.697
  pending              0.693
  clashes              0.692
  discrimination       0.691
  enactment            0.688

## Questions and ideas

Note that the first two models overlap the era of Residential Segregation Ordinances. The last model is after the SCOTUS ruling in *Buchanan v. Wharley* but ordinances still occur in close similarity to segregation in the corpus. This reflects the lingering redsidential segregation ordinances that remained enforced within municipalities after being struck down by SCOTUS and the efforts of the NAACP to bring awareness of housing inequalities through activism and court cases.

=======
# 02_explore_model

I am interested in mining this corpus to see what 
is being said about Residential Segregation Ordinances in these sources. For this reason, left my WORD as "segregation" but I changed the SEED WORDS to words that will be more helpful to creating a semantic field that explores my research question. I chose "residence, dwelling, law, block, home, ordinance". 

First run: 
Model: 1910-1916  (10,433 words)

1. Nearest words to 'segregation'  (1.0 = identical direction, 0 = unrelated)
   ordinance              0.795
   ordinances             0.759
   protesting             0.717
   discrimination         0.712
   ghetto                 0.711
   invalid                0.704
   involving              0.699
   jim-crow               0.687
   opposing               0.679
   valid                  0.679
   anti-intermarriage     0.677
   proposal               0.675
   ruling                 0.666
   constitutionality      0.664
   un-american            0.660

2. Words nearest to the average of ['residence', 'dwelling', 'law', 'block', 'home', 'ordinance']
   limits, occupants, occupying, congested, abolishing, plot, residential, permits, divorce, repair, outskirts, instituted, foree, reside, wires, conveyance, flats, compelling, purchasing, thereof

# this run captures the legal fights that were beginning in Baltimore and Lexington concerning residential segregation ordinance. More importantly, it captures the way in which DuBose and others were framining the narrative around these ordinances. They are "un-american, (not)valid, and of questionalble constitutionality. The words nearest the SEED WORDS document how muncipalities were attacking Black communities through property lawfare (permits, technicalities of building codes, surveying, ordinances etc.)

First Run 1917-1923: 
# Model: 1917-1923  (12,289 words)

1. Nearest words to 'segregation'  (1.0 = identical direction, 0 = unrelated)
   ordinances             0.745
   jim-crowism            0.742
   ordinance              0.734
   discrimination         0.722
   lawlessness            0.712
   jim-crow               0.702
   residential            0.700
   unequal                0.688
   crow                   0.681
   discriminatory         0.679
   abolish                0.679
   unconstitutional       0.677
   legislation            0.674
   violence               0.668
   disfranchisement       0.662

2. Words nearest to the average of ['residence', 'dwelling', 'law', 'block', 'home', 'ordinance']
   abode, lease, litigation, tenement, occupy, overcrowded, occupancy, saloon, annex, attendant, residential, exercising, leased, regulate, rio, assessed, boundaries, baggage, permitting, adjoining

# Demonstrates the legal fight over ordinances. Also captures the violence of the era and the discrimination against/suspecion of black spaces (saloon, overcrowded, tenement).

First Run 1924-1930
Model: 1924-1930  (17,607 words)

1. Nearest words to 'segregation'  (1.0 = identical direction, 0 = unrelated)
   residential            0.834
   unconstitutional       0.722
   ordinances             0.711
   legality               0.697
   pending                0.693
   clashes                0.692
   discrimination         0.691
   enactment              0.688
   disfranchisement       0.685
   clauses                0.683
   enacted                0.682
   flagrant               0.682
   discriminatory         0.677
   evade                  0.677
   legislation            0.672

2. Words nearest to the average of ['residence', 'dwelling', 'law', 'block', 'home', 'ordinance']
   precinct, adjoining, sewerage, suburban, tubercular, lung, premises, regulated, structures, reformatory, suburbs, okfuskee, four-room, corporate, kitchens, overcrowded, inspectors, overflow, vacated, occupants

   =======
   Change over time:
   Question: How has segregation changed over time in each of the models?

   Answer: It did not really change that much. (Segregation was not the best word choice for this task when using a black history corpus).

   1. How often 'segregation' appears
   1910-1916: 720 times
   1917-1923: 271 times
   1924-1930: 586 times

2. Nearest neighbors in each period
   1910-1916: ordinance, ordinances, protesting, discrimination, ghetto, invalid, involving, jim-crow, opposing, valid
   1917-1923: ordinances, jim-crowism, ordinance, discrimination, lawlessness, jim-crow, residential, unequal, crow, discriminatory
   1924-1930: residential, unconstitutional, ordinances, legality, pending, clashes, discrimination, enactment, disfranchisement, clauses

3. How far 'segregation' moved  (0 = no change)
   1910-1916 -> 1917-1923: 0.27
   1917-1923 -> 1924-1930: 0.19
   1910-1916 -> 1924-1930: 0.23
   'segregation' moved more than 29% of the 1,083 words used 200+ times in both periods

Lets try 'ordinance' instead:

Results for Ordinance:
1. How often 'ordinance' appears
   1910-1916: 246 times
   1917-1923: 105 times
   1924-1930: 108 times

2. Nearest neighbors in each period
   1910-1916: segregation, ordinances, invalid, valid, ghetto, injunction, anti-intermarriage, passage, amended, proposing
   1917-1923: unconstitutional, injunction, sustained, ordinances, violating, validity, repeal, permitting, constitutionality, statutes
   1924-1930: unconstitutional, enactment, injunction, repeal, violating,statute, enacted, clause, violation, ordinances

3. How far 'ordinance' moved  (0 = no change)
   1910-1916 -> 1917-1923: 0.23
   1917-1923 -> 1924-1930: 0.15
   1910-1916 -> 1924-1930: 0.22
   'ordinance' moved more than 25% of the 1,083 words used 200+ times in both periods

   Lastly, lets try 'residential':

   1. How often 'residential' appears
   1910-1916: 40 times
   1917-1923: 42 times
   1924-1930: 132 times

2. Nearest neighbors in each period
   1910-1916: theatres, residences, residents, districts, neighborhoods, railways, ordinances, conveyance, alleys, restaurants
   1917-1923: city's, prohibit, congested, jim-crow, ordinances, areas, overcrowded, overcrowding, prohibiting, dwellings
   1924-1930: segregation, clashes, suburban, ordinances, prostitution, subdivision, districts, congested, peonage, clauses

3. How far 'residential' moved  (0 = no change)
   1910-1916 -> 1917-1923: 0.16
   1917-1923 -> 1924-1930: 0.22
   1910-1916 -> 1924-1930: 0.19
   'residential' moved more than 14% of the 1,083 words used 200+ times in both periods

======
Gender and a word:

first attempt: residential

Model: 1924-1930
Women words: woman, women, she, her, hers, herself, girl, girls
Men words:   man, men, he, his, him, himself, boy, boys

The 189 words closest to 'residential' (similarity 0.52 or more), sorted by which way they lean:

  Lean toward WOMEN:
   delaware (+0.13), city's (+0.13), playgrounds (+0.13), residence (+0.13), ruling (+0.12), gary (+0.12), similarly (+0.11), acute (+0.11), resort(+0.09), insures (+0.09), appeals (+0.09), louisville (+0.08), cities (+0.08), separation (+0.08), supreme (+0.07), asbury (+0.07), separate (+0.07), parks (+0.06), ruled (+0.06), towns (+0.06)

  Lean toward MEN:
   wholesale (-0.23), disfranchisement (-0.17), violence (-0.17), farming(-0.17), inevitably (-0.16), agitation (-0.15), transfer (-0.15), corporations (-0.14), operations (-0.13), specifically (-0.13), businesses (-0.13), enforce (-0.13), primaries (-0.13), lynching (-0.13), primary (-0.13), violation (-0.12), intermarriage (-0.12), administrative (-0.11), enacted (-0.11), divide (-0.11)

  ('residential' itself scores -0.03)

Saved the plot to plots/gender_residential_1924-1930.png

# its interesting the actual court case names lean more towards women (delaware, louisville, asbury)
 # words related to aggression and violence lean more to men (agitation, violation)

 Second attempt: Ordinance
 Model: 1924-1930
Women words: woman, women, she, her, hers, herself, girl, girls
Men words:   man, men, he, his, him, himself, boy, boys

The 189 words closest to 'ordinance' (similarity 0.53 or more), sorted bywhich way they lean:

  Lean toward WOMEN:
   delaware (+0.13), ruling (+0.12), adopted (+0.12), similarly (+0.11), resort (+0.09), authorities (+0.09), insures (+0.09), appeals (+0.09), separation (+0.08), supreme (+0.07), testimony (+0.07), ruled (+0.06), council (+0.06), utterly (+0.05), jurisdiction (+0.05), declared (+0.05), court (+0.05), representation (+0.04), legislation (+0.04), protest (+0.04)

  Lean toward MEN:
   election (-0.21), ballot (-0.19), democratic (-0.19), voter (-0.19), mob (-0.19), nomination (-0.18), alleged (-0.18), procedure (-0.17), disfranchisement (-0.17), ticket (-0.17), violence (-0.17), defeat (-0.16), conviction (-0.16), dyer (-0.15), agitation (-0.15), transfer (-0.15), anti-lynching (-0.14), vote (-0.14), action (-0.14), process (-0.14)

  ('ordinance' itself scores +0.03)

Saved the plot to plots/gender_ordinance_1924-1930.png

Second run with 'ordinance' and changed the year to 1910-1916

Model: 1910-1916
Women words: woman, women, she, her, hers, herself, girl, girls
Men words:   man, men, he, his, him, himself, boy, boys

The 109 words closest to 'ordinance' (similarity 0.53 or more), sorted bywhich way they lean:

  Lean toward WOMEN:
   amusement (+0.13), relief (+0.12), amendment (+0.12), assembly (+0.11), louisville (+0.10), adopted (+0.10), protests (+0.10), constantly (+0.08), complaint (+0.08), agitation (+0.08), causes (+0.08), park (+0.08), resolutions (+0.07), provision (+0.07), film (+0.05), residents (+0.05), operation (+0.05), outrage (+0.04), council (+0.04), appeals (+0.04)

  Lean toward MEN:
   mayor (-0.14), bills (-0.13), railway (-0.12), segregation (-0.11), principle (-0.11), verdict (-0.11), passage (-0.10), determined (-0.09), similar (-0.08), measures (-0.08), attempt (-0.08), unfair (-0.08), courtesy (-0.08), introduced (-0.07), violation (-0.07), appealed (-0.07), disfranchisement (-0.07), propose (-0.06), bill (-0.06), openly (-0.06)

  ('ordinance' itself scores -0.07)

Saved the plot to plots/gender_ordinance_1910-1916.png
