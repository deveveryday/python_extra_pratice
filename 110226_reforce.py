# -*- coding: utf-8 -*-

"""https://www.notion.so/Monitoria-SENAI-304819ac28e58097a42de584d0991919

*Exercícios de reforço com João antes da aula 18h*

1.

Peça a idade de uma pessoa e diga:

"Maior de idade" se tiver 18 ou mais

"Menor de idade" caso contrário

2.

Peça um número e diga:

"Número positivo"

"Número negativo"

"Zero"

3.

Peça a temperatura e diga:

"Frio" se for menor que 15

"Agradável" entre 15 e 25

"Quente" acima de 25

4.

Peça a nota de um aluno e diga:

"Aprovado" se nota ≥ 6

"Reprovado" se nota < 6

5.

Peça um número e diga se ele é:

Par

Ímpar

6.

Peça o salário e diga:

"Salário baixo" se < 2000

"Salário médio" entre 2000 e 5000

"Salário alto" acima de 5000

🟡 Nível Intermediário

Agora com mais condições e lógica.

7.

Peça a idade e classifique:

Criança: até 12

Adolescente: 13 a 17

Adulto: 18 a 59

Idoso: 60+

8.

Peça três números e diga qual é o maior.

9.

Peça o turno de estudo:

M → "Bom dia"

T → "Boa tarde"

N → "Boa noite"

Outro → "Turno inválido"

10.

Peça o preço de um produto:

Até 100 → desconto de 10%

101 a 500 → desconto de 5%

Acima de 500 → sem desconto
Mostre o preço final.

11.

Peça o peso de uma bagagem:

Até 23kg → "Sem taxa"

23 a 32kg → "Taxa extra"

Acima de 32kg → "Bagagem não permitida"

12.

Peça o ano de nascimento e calcule:

Se pode votar (idade ≥ 16)

Se o voto é obrigatório (18 a 70)

Se é facultativo (16–17 ou acima de 70)

🔴 Nível Difícil (apenas 2, como você pediu)
13.

Peça o valor de um empréstimo e o salário da pessoa.

Regra:

A parcela não pode ultrapassar 30% do salário.

Considere o empréstimo dividido em 12 parcelas.

Mostre:

"Empréstimo aprovado"

"Empréstimo negado"

14.

Sistema de login simples:

Peça:

Usuário

Senha

Regras:

Usuário correto: admin

Senha correta: 1234

Respostas:

Ambos corretos → "Login realizado"

Usuário correto e senha errada → "Senha incorreta"

Usuário errado → "Usuário não encontrado"
"""

#1
user_age = int(input("Type your age here::: "))
system_message = ""

if user_age >= 18:
  system_message = "You are legal adult now."
else:
  system_message = "You aren't adult."

print(system_message)

"""Peça um número e diga:

"Número positivo"
"Número negativo"
"""

#2
number_typed = int(input("Tell me a number>>"))
number_message = ""

if number_typed >= 0:
  number_message = f"You gave a positive number. {number_typed}"
else:
  number_message = f"You gave a negative number! =x {number_typed}"

print(number_message)



"""3.

Peça a temperatura e diga:

"Frio" se for menor que 15

"Agradável" entre 15 e 25

"Quente" acima de 25
"""

#3

temp_typed = float(input("Hi, what's the temperature right now?? :: "))

if temp_typed < 15:
  temperature_message = "It's cold, huh?"
elif temp_typed >=15 and temp_typed < 15:
  temperature_message = "Uu it's cool and warm right now :)"
elif temp_typed > 15:
  temperature_message = "Ops very hot!!!"

print(f"\n%%%%%% {temperature_message} %%%%%%")

"""4.
Peça a nota de um aluno e diga:

"Aprovado" se nota ≥ 6

"Reprovado" se nota < 6
"""

school_test_score = int(input(" Say what is your score in the finals test  "))

if school_test_score >= 6:
  school_message = f"Your are aproved!! {school_test_score} "
else:
  school_message = f"Oooo you are reproved! {school_test_score}"

print(f"\n{school_message}")

"""5.

Peça um número e diga se ele é:

Par

Ímpar
"""

#5
number_typed = int(input("Tell me a number>>"))
number_message = ""

if number_typed % 2 == 0:
  number_message = f"You gave a positive number. {number_typed}"
else:
  number_message = f"You gave a negative number! =x {number_typed}"

print(number_message)

"""6.

Peça o salário e diga:

"Salário baixo" se < 2000

"Salário médio" entre 2000 e 5000

"Salário alto" acima de 5000
"""

#6

employee_month_salary = float(input("Hi, which is your monthly "))

"""7. Peça a idade e classifique:

Criança: até 12

Adolescente: 13 a 17

Adulto: 18 a 59

Idoso: 60+
"""

#7
person_age = int(input("Tell many how many years you got:: "))

if person_age <= 12:
  feedback = "That's a children"
elif person_age > 12 and person_age <= 17:
  feedback = "Teenager"
elif person_age > 18 and person_age < 59:
  feedback = "It´s an adult age"
else:
  feedback = "Elder´s place"

print(f"The age system\n::::: {feedback} ... {person_age}")

"""8.
Peça três números e diga qual é o maior.
"""

#8

first_number = float(input("Tell me a luck number"))
second_number = float(input("Hmm, tell me another number"))
third_number = float(input("Now the last one, come on"))

if first_number > second_number and first_number > third_number:
  greatest_number = first_number
elif second_number > first_number and second_number > third_number:
  greatest_number = second_number
else:
  greatest_number = third_number

print(f"the bigger NUMBEEERRRRRR::: {greatest_number}")



"""9. Peça o turno de estudo:

M → "Bom dia"

T → "Boa tarde"

N → "Boa noite"

Outro → "Turno inválido"
"""

#9

class_time = input("Tell me your turn in your school:: ")

if class_time == "M":
  system_feedback = "Good morning ☕"
elif class_time == "T":
  system_feedback = "Good afternoon 🎶"
else:
  system_feedback = "Good evening 😴"

print(f"{system_feedback}, dear!")

"""10. Peça o preço de um produto:

Até 100 → desconto de 10%

101 a 500 → desconto de 5%

Acima de 500 → sem desconto Mostre o preço final.
"""

#10
product_price = float(input("How much did you spend?? "))
disccount = 10

if product_price <= 100:
  final_message = f"{product_price - ((product_price * disccount)/100)} ---- {product_price * (disccount/100)}"

print(final_message)

"""
Peça o peso de uma bagagem:

Até 23kg → "Sem taxa"

23 a 32kg → "Taxa extra"

Acima de 32kg → "Bagagem não permitida"
"""

#11

baggage = int(input("Tell me your baggage weight\n"))

if baggage < 23:
  message = "No tax"
elif baggage >= 23 and baggage < 32:
  message = "Extra tax $$"
else:
  message = "Your baggage isn't allowed"


print(f">> {message}")

"""
12.

Peça o ano de nascimento e calcule:

Se pode votar (idade ≥ 16)

Se o voto é obrigatório (18 a 70)

Se é facultativo (16–17 ou acima de 70)

🔴 Nível Difícil (apenas 2, como você pediu) 13."""

#12
from datetime import date

birth_date = input("What is your birth year date xxxx")
age = 2026 - birth_date

if age <= 16:
  vote_message = "You can vote already"
elif age > 18 and age < 70: