import json
import os

def load_rules(path="data/rules.json"):
    with open(path, "r") as file:
        return json.load(file)

def find_combinations(vuln, rules, reverse=False):
    results = []
    for rule in rules:
        if reverse and vuln in rule.get("combined_with", []):
            results.append(rule)
        elif not reverse and rule.get("base_vuln") == vuln:
            results.append(rule)
    return results

def export_results(results, filename):
    with open(filename, "w") as f:
        for r in results:
            f.write(json.dumps(r, indent=4) + ",")

def calculate_combination_risk(R1: float, R2: float, C: float) -> float:
    R1 = min(max(R1, 0), 10)
    R2 = min(max(R2, 0), 10)
    C = max(C, 0.1)  # защита от деления на 0
    result = 10 * (1 - (1 - R1 / 10) * (1 - R2 / 10) * (1 / C))
    return round(min(result, 10), 2)