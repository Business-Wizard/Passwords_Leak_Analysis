# Context

One day we all get the message -
A notification that beems across your phone or chimes into your inbox. . .

>Dear Customer, \
we’re letting you know that we detected unusual activity on your account and are taking action to. . .

“Was my information stolen from my bank, my employer, or that one website I love to read at night”? [^xkcd]  
How the bad-guys managed to steal or purchase your information, you’ll never know for sure.  But of all the ways you can better protect you and your family against cyber criminals, there is one advice you’ve heard the most.  And it’s also the one you’ve agreed with the most, told yourself you’d commit to it, and then promptly forgot about again at least until the news of another data breach slides across your phone. [^breachnotice]

<center>Create a strong password!</center>

---
What really makes a strong password anyway?

- Is it having a specific date that you haven’t told anyone?
- Is it the amount of fancy characters you can find on your keyboard?
- Or perhaps the cat ladies of the world have the true secret to fighting cyber criminals after all - just make a password with all of the names of your cats.[^cat_lady]

## Data

The datasets used in this project provide a variety in both source, context, and size.  The passwords are sourced from notable data breaches such as Linkedin [^linkedin_count] and Rock You, as well as an aggregate database totaling over 560 million passwords.[^ibeenpwned]  My datasets are facially simple - they are a collection of either the passwords in plaintext form.  All other features were derived by analyzing the password plaintext (e.g length of password and count of lowercase letters used).

Two other features highlighted during this analysis was an overall score from 0-4 to represent how strong each password was, as well as an estimate for how many guesses a motivated hacker would need before breaking each password.[^zxcvbn]

---

## Goals & Minimum Viable Product

1. Create a novel data pipeline to prepare the datasets to a common standard.
2. Practice methods of data manipulation that scale well with datasets in excess of 3-25GB.
3. Create code using Object-Oriented Principles that can be further developed in the future capstones or as a valuable open-source product.


## Data Description


## Data Exploration


## Password Recommendations

Try out the Password Strength Tool [here](https://business-wizard.github.io/password_strength_capstone01/)!

1. Length > 14
   -  Combine 4 or more **uncommon** words
   -  for a memorable phrase that you can imagine
   -  Add symbols and numbers between each word
2. Length > 10
   - Use 







## Next Steps

1. Add Password Strength Indicator to Project Website
2. Add capability for pipeline to use multiple cores
     - Dask, Rapids, Spark as options
3. Standardize larger datasets for use in future research.
4. Explore use of Machine Learning models such as LSTM and Markov based models.







### Motivating Research & Extended Resources

1. [A Machine Learning Approach to Predicting Passwords -Christoffer Olsen](http://www2.imm.dtu.dk/pubdb/edoc/imm7088.pdf)
2. [PassGAN: A Deep Learning Approach for Password Guessing](https://arxiv.org/pdf/1709.00440.pdf)
3. [hashcat](https://hashcat.net/hashcat/)
4. [hashcat setup guide for Ubuntu](https://www.alexanderjsingleton.com/infosexy-how-to-use-hashcat-to-crack-passwords-in-ubuntu-18-04/)
5. [Comparison of Dictionary Attack Rulesets](https://notsosecure.com/one-rule-to-rule-them-all/)

---
#### Footnotes

[^xkcd]: [xkcd](https://xkcd.com/2374/)

[^breachnotice]: Months after the breach occured

[^cat_lady]: If you have less than four, read on

[^linkedin_count]: 61 million passwords

[^ibeenpwned]: [Aggregate Dataset of Password](https://haveibeenpwned.com/)

[^zxcvbn]: Made possible by the work of [Dan Wheeler](https://dropbox.tech/security/zxcvbn-realistic-password-strength-estimation)
