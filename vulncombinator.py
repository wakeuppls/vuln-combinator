import argparse
from core import load_rules, find_combinations, export_results, calculate_combination_risk

def parse_args():
    parser = argparse.ArgumentParser(
        description="VulnCombinator - анализатор цепочек уязвимостей"
    )
    parser.add_argument('--vuln', type=str, help="Указать уязвимость для анализа")
    parser.add_argument('--reverse', action='store_true', help="Искать обратные комбинации")
    parser.add_argument('--export', type=str, help="Сохранить результат в файл")
    parser.add_argument('--risk', nargs=3, type=float, metavar=('R1', 'R2', 'C'),
                        help="Рассчитать итоговую критичность для пары уязвимостей и коэффициента усиления")
    return parser.parse_args()


def main():
    ascii_art = r"""
 ##   ##            ###                ####                     ###        ##                         ##
 ##   ##             ##               ##  ##                     ##                                   ##
  ## ##   ##  ##     ##     #####    ##        ####    ##  ##    ##       ###     #####     ####     #####    ####    ######
  ## ##   ##  ##     ##     ##  ##   ##       ##  ##   #######   #####     ##     ##  ##       ##     ##     ##  ##    ##  ##
   ###    ##  ##     ##     ##  ##   ##       ##  ##   ## # ##   ##  ##    ##     ##  ##    #####     ##     ##  ##    ##
   ###    ##  ##     ##     ##  ##    ##  ##  ##  ##   ##   ##   ##  ##    ##     ##  ##   ##  ##     ## ##  ##  ##    ##
    #      ######   ####    ##  ##     ####    ####    ##   ##  ######    ####    ##  ##    #####      ###    ####    ####

                                                      VulnCombinator | v1.0
    """

    print(ascii_art)
    args = parse_args()

    if args.risk:
        R1, R2, C = args.risk
        score = calculate_combination_risk(R1, R2, C)
        print(f"[+] Итоговая критичность (комбинация): {score:.2f}")
        return

    if args.vuln:
        rules = load_rules()
        matches = find_combinations(args.vuln, rules, reverse=args.reverse)

        if matches:
            print(f"[+] Найдено {len(matches)} возможных комбинаций:")
            for m in matches:
                print(f"  - {m['base_vuln']} + {', '.join(m['combined_with'])} → {m['goal']} ({m['risk_score']})")
                print(f"    Описание: {m['description']}")
        else:
            print("[-] Комбинации не найдены.")

        if args.export:
            export_results(matches, args.export)
            print(f"[+] Результаты сохранены в {args.export}")

if __name__ == "__main__":
    main()