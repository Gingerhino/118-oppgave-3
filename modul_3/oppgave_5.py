alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

# Jeg tror at det blir: true
print(alder > aldersgrense)

# Jeg tror at det blir: true
print(alder == 31)

# Jeg tror at det blir: true
print(alder != aldersgrense)

# Jeg tror at det blir: false
print(alder <= aldersgrense)

# Jeg tror at det blir: true
print(navn == "Michael")

# Jeg tror at det blir: false
print(navn == "michael")

# Jeg tror at det blir: true
print(antall_studenter >= 30)

# Jeg tror at det blir: true
print(alder + 5 > antall_studenter)


# --- Refleksjon --- 

# De er ulike på grunn av at varibalen er skrevet med en stor M ikke en liten M

# Forskjellen er at = betyr at det er det vi har bestemt at det skal være, foreksempel navn er Michael
# Imens == betyr at de er det samme så, i alder == 31, har alder allerede en verdi som er 31 så det vi sier er at 31 er det samme som 31

# Eg trur den følger aritmetisk først

# Eg trur det blir nyttig i if statements der man vil si hvis dette skjer så er det sant, hvis ikke er det usant