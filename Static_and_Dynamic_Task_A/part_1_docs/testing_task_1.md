### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# Need == or it will won't return with true or false. Else is also missing syntax : to allow else statement to work.

  def check_for_ace(self, card):
    if card.value = 1: #==
      return True
    else#:
      return False
   
#def instead of dif, and missing comma in the parameters which will provide error. Missing number for card(1), and indentation is wrong
  dif highest_card(self, card1 card2): #def and missing comma
  if card1.value > card2.value:
    return card#1
  else:
    return card2
  #wrong indentation

#full indentation of the function below sitting outside the class. total needs to equal 0 to start a count. return statement should sit outside the loop.

def cards_total(self, cards):
  total  # =0
  for card in cards:
    total += card.value
    return "You have a total of" + total #needs to be outside of the loop and formatting for return statement.
  
```
