## Vulnerability Combinator (VulnCombinator)

**VulnCombinator** — это CLI-инструмент, предназначенный для анализа возможных комбинаций уязвимостей и оценки совокупного риска. Он помогает специалистам по безопасности выявлять потенциальные цепочки атак на основе заданной уязвимости.

---

### Возможности

* Поиск всех возможных комбинаций уязвимостей по `rules.json`
* Обратный поиск (где уязвимость встречается в связке, а не как базовая)
* Расчет комбинированного риска с учетом коэффициента взаимодействия
* Экспорт результатов в файл

---

### Структура проекта

```
vulncombinator/
├── core.py         # Логика поиска и расчета
├── vulncombinator.py         # CLI-интерфейс
├── rules.json      # База правил с комбинациями
```

---

### Установка

```bash
git clone https://github.com/wakeuppls/vuln-combinator.git
cd vuln-combinator
python vulncombinator.py --help
```

---

### Примеры использования

Найти все комбинации для XSS:

```bash
python vulncombinator.py --vuln XSS
```

Найти все случаи, где XSS используется в связках (не только как базовая уязвимость):

```bash
python vulncombinator.py --vuln XSS --reverse
```

Сохранить результат в файл:

```bash
python vulncombinator.py --vuln XSS --reverse --export results.txt
```

Рассчитать комбинированный риск:

```bash
python vulncombinator.py --risk 7.2 5.0 1.3
```

---

### Пример правила (`rules.json`)

```json
{
  "base_vuln": "XSS",
  "combined_with": ["CSRF"],
  "goal": "Account takeover",
  "risk_score": 8.5,
  "description": "Use XSS to inject a malicious form that exploits CSRF for unauthorized actions."
}
```

---

### Экспорт результатов

Флаг `--export <file>` позволяет сохранить найденные комбинации в текстовый файл.

---

### Модель оценки риска

Комбинированный риск рассчитывается по формуле:

```
R_combo = 10 × (1 - (1 - R1/10) × (1 - R2/10) × 1/C)
```

где:

* `R1`, `R2` — индивидуальные риски уязвимостей (по шкале 0–10)
* `C` — коэффициент взаимодействия

---

Если хочешь, я могу сразу добавить этот файл в проект.
