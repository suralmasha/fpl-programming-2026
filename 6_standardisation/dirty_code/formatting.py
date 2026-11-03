# Нарушения: импорты, пробелы, отступы и длинные строки.
import sys,os
from pathlib import Path
import json


def save_report( words,path ):
  counts={word:words.count(word) for word in set(words)}
  report={"words":words,"counts":counts,"total":len(words),"description":"Пример отчета для демонстрации автоматического форматирования Python-кода"}
  Path(path).write_text(json.dumps(report,ensure_ascii=False),encoding="utf-8")
  return counts


if __name__=="__main__":
  print(save_report(["кот","пес","кот"],"report.json"))
