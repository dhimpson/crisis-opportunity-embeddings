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

