# A model is tested on data it never saw during training

Sam can explain that a dataset is split into a training set, which the model learns from, and a test set, which is held out and used only to measure the model.
Sam also sees why: a model's score on the data it learned from is too optimistic, so only data it has never seen shows how it will do on new data.

**Evidence:** Described the test set, in his own words, as the part of the data the model "doesn't get to study," and said that testing on the training data would be like grading a student on the exact questions they practiced.

**Implications:** Split sizes, such as which part of an 80/20 split is the test set, came up only briefly.
Keeping the test set unseen while choosing between models was mentioned but not practiced, and overfitting has not been taught yet.
