from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
def unique_koala_facts(requested_amount):
    facts = []
    i = 0
    while len(facts) < requested_amount:
        fact = random_koala_fact()
        if fact not in facts:
            facts.append(fact)
        if i == 1000:
            break
        i += 1
    return facts

def num_joey_facts():
  first_fact = random_koala_fact()
  first_fact_count = 0
  joey_count = 0
  joey_facts = []
  while first_fact_count < 10:
      fact = random_koala_fact()
      if fact == first_fact:
        first_fact_count += 1
      if 'joey' in fact and fact not in joey_facts:
        joey_count += 1
        print(fact)
        joey_facts.append(fact)
  return joey_count

def koala_weight():
    while True:
        fact = random_koala_fact()
        if 'kg' in fact:
            start_of_weight = fact.find('kg')-2
            weight = int(fact[start_of_weight:start_of_weight+2])
            break
    return weight

if __name__ == "__main__":
    print(random_koala_fact())

    print(unique_koala_facts(10))

    print(num_joey_facts())

    print(koala_weight())