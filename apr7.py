#conda install jupyter pandas matplotlib ipywidgets
#homework 2: https://github.com/pybait/hw2-Nan227.gity


class Person2(oject):
  # ... or pass, to keep the program running without interupting 
  def __init__(self, first,last,yr):
    self.first_name = first
    self.last_name = last
    self.birth_year = yr
Person("Barack","Obama",1961)

# p.foo => attibute error
# p.firstname = "Barack"
# class Person:
  # p= Person()
  # p.firstname = "Barack"
  # p.lastname = "Obama"
  # p.birthyear = 1961

  # p2= Person()
  # p.firstname = "Nan"
  # p.lastname = "Obb"
  # p.birthyear = 1981
  #------------------------------------------
class Person:
  # change the name
  def __init__(p, first, last, year):
  # def Person_init(p,first,last,year):
    p.firstname = first
    p.lastname = last
    p.birthyear = year
  def get_age(p):
    return 2023 - p.birthday 

  def to_string(p):
    return f"<{p.firstname} {p.lastname}, {p,birthday}>"

  p1 = Person("Barack","Obama", 1961)
  p2 = Person("Justin","Bieber", 1994)

  #p1= Person()
  #Person.init(p, "Barack","Obama", 1961)
 # p1 = Person("Barack","Obama", 1961)
  # p2 = Person()
  # Person.init(p2, "Justin","Bieber", 1994)

 # p2 = Person("Justin","Bieber", 1994)
  # Person is a tpye
  # Person . get_age(p1)
  #62
  # or p1 . get_get() #62 => p1.get_age()
  # p2.get_age() = > 29
  # p1 => '< __main__.Person at 0x7fa07db681c0>'
  # you can use Jupiter lab

  # jupiternotebook => 3 things =>file format, user interface, one more