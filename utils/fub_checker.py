
bad_words = [
    {"word": " хуй ", "lens": len("хуй")},
    {"word": " хуя ", "lens": len("хуя")},
    {"word": " хую ", "lens": len("хую")},
    {"word": " хуем ", "lens": len("хуем")},
    {"word": " хуями ", "lens": len("хуями")},
    {"word": " хуё ", "lens": len("хуё")},
    {"word": " хуёв ", "lens": len("хуёв")},
    {"word": " хуёвый ", "lens": len("хуёвый")},
    {"word": " хуёво ", "lens": len("хуёво")},
    {"word": " нахуй ", "lens": len("нахуй")},
    {"word": " нахуя ", "lens": len("нахуя")},
    {"word": " нахую ", "lens": len("нахую")},
    {"word": " нахуй ", "lens": len("нахуй")},
    {"word": " похуй ", "lens": len("похуй")},
    {"word": " похуя ", "lens": len("похуя")},
    {"word": " похую ", "lens": len("похую")},
    {"word": " охуй ", "lens": len("охуй")},
    {"word": " охуя ", "lens": len("охуя")},
    {"word": " охую ", "lens": len("охую")},
    {"word": " охуел ", "lens": len("охуел")},
    {"word": " охуела ", "lens": len("охуела")},
    {"word": " охуели ", "lens": len("охуели")},
    {"word": " охуеть ", "lens": len("охуеть")},
    {"word": " охуенно ", "lens": len("охуенно")},
    {"word": " охуенный ", "lens": len("охуенный")},
    {"word": " залупа ", "lens": len("залупа")},
    {"word": " залупу ", "lens": len("залупу")},
    {"word": " залупой ", "lens": len("залупой")},
    {"word": " залупе ", "lens": len("залупе")},
    {"word": " залупы ", "lens": len("залупы")},
    {"word": " залупаться ", "lens": len("залупаться")},
    {"word": " пенис ", "lens": len("пенис")},
    {"word": " пениса ", "lens": len("пениса")},
    {"word": " пенису ", "lens": len("пенису")},
    {"word": " пенисом ", "lens": len("пенисом")},
    {"word": " пенисе ", "lens": len("пенисе")},
    {"word": " пенисы ", "lens": len("пенисы")},
    {"word": " пенисов ", "lens": len("пенисов")},
    {"word": " гитлер ", "lens": len("гитлер")},
    {"word": " гитлера ", "lens": len("гитлера")},
    {"word": " гитлеру ", "lens": len("гитлеру")},
    {"word": " гитлером ", "lens": len("гитлером")},
    {"word": " гитлере ", "lens": len("гитлере")},
    {"word": " гитлеры ", "lens": len("гитлеры")},
    {"word": " гитлеров ", "lens": len("гитлеров")},
    # обходные варианты: x*й, xуй, х*й, x.y и т.п.
    {"word": " x*й ", "lens": len("x*й")},
    {"word": " xуй ", "lens": len("xуй")},
    {"word": " х*й ", "lens": len("х*й")},
    {"word": " х*уй ", "lens": len("х*уй")},
    {"word": " x*ya ", "lens": len("x*ya")},
    {"word": " x*ю ", "lens": len("x*ю")},
    {"word": " x*y ", "lens": len("x*y")},
    {"word": " xуя ", "lens": len("xуя")},
    {"word": " xую ", "lens": len("xую")},
    {"word": " xуем ", "lens": len("xуем")},
    {"word": " xуё ", "lens": len("xуё")},
    {"word": " xуёв ", "lens": len("xуёв")},
    {"word": " наx*й ", "lens": len("наx*й")},
    {"word": " наxуй ", "lens": len("наxуй")},
    {"word": " нах*й ", "lens": len("нах*й")},
    {"word": " поx*й ", "lens": len("поx*й")},
    {"word": " поxуй ", "lens": len("поxуй")},
    {"word": " поху* ", "lens": len("поху*")},
    {"word": " оx*й ", "lens": len("оx*й")},
    {"word": " оxуй ", "lens": len("оxуй")},
    {"word": " оху* ", "lens": len("оху*")},
    # латинские двойники
    {"word": " xyй ", "lens": len("xyй")},
    {"word": " xyя ", "lens": len("xyя")},
    {"word": " xую ", "lens": len("xую")},
    {"word": " пeнис ", "lens": len("пeнис")},
    {"word": " гитлeр ", "lens": len("гитлeр")},
    {"word": " зaлупа ", "lens": len("зaлупа")},
    # составные / слитные
    {"word": " хуйня ", "lens": len("хуйня")},
    {"word": " хуйни ", "lens": len("хуйни")},
    {"word": " хуйнёй ", "lens": len("хуйнёй")},
    {"word": " хуёвина ", "lens": len("хуёвина")},
    {"word": " хуёво ", "lens": len("хуёво")},
    {"word": " нахуй ", "lens": len("нахуй")},
    {"word": " нахуй ", "lens": len("нахуй")},
    {"word": " нихуя ", "lens": len("нихуя")},
    {"word": " нихуй ", "lens": len("нихуй")},
    {"word": " дохуя ", "lens": len("дохуя")},
    {"word": " дохуй ", "lens": len("дохуй")},
    {"word": " схуя ", "lens": len("схуя")},
    {"word": " схуй ", "lens": len("схуй")},
    {"word": " распиздяй ", "lens": len("распиздяй")},
    {"word": " пизда ", "lens": len("пизда")},
    {"word": " пизду ", "lens": len("пизду")},
    {"word": " пиздой ", "lens": len("пиздой")},
    {"word": " пизде ", "lens": len("пизде")},
    {"word": " пизды ", "lens": len("пизды")},
    {"word": " пиздец ", "lens": len("пиздец")},
    {"word": " пиздато ", "lens": len("пиздато")},
    {"word": " пиздатый ", "lens": len("пиздатый")},
    {"word": " блядь ", "lens": len("блядь")},
    {"word": " бляди ", "lens": len("бляди")},
    {"word": " блядью ", "lens": len("блядью")},
    {"word": " блядский ", "lens": len("блядский")},
    {"word": " бля ", "lens": len("бля")},
    {"word": " бляха ", "lens": len("бляха")},
    {"word": " ебать ", "lens": len("ебать")},
    {"word": " ебала ", "lens": len("ебала")},
    {"word": " ебали ", "lens": len("ебали")},
    {"word": " ебаный ", "lens": len("ебаный")},
    {"word": " ебанутый ", "lens": len("ебанутый")},
    {"word": " ебальник ", "lens": len("ебальник")},
    {"word": " ебля ", "lens": len("ебля")},
    {"word": " ебло ", "lens": len("ебло")},
    {"word": " ебнуть ", "lens": len("ебнуть")},
    {"word": " ебнуться ", "lens": len("ебнуться")},
    {"word": " заебал ", "lens": len("заебал")},
    {"word": " заебала ", "lens": len("заебала")},
    {"word": " заебали ", "lens": len("заебали")},
    {"word": " заебать ", "lens": len("заебать")},
    {"word": " заебись ", "lens": len("заебись")},
    {"word": " заебато ", "lens": len("заебато")},
    {"word": " отъебись ", "lens": len("отъебись")},
    {"word": " отъебитесь ", "lens": len("отъебитесь")},
    {"word": " уебок ", "lens": len("уебок")},
    {"word": " уебка ", "lens": len("уебка")},
    {"word": " уебище ", "lens": len("уебище")},
    {"word": " уебан ", "lens": len("уебан")},
    {"word": " мудак ", "lens": len("мудак")},
    {"word": " мудака ", "lens": len("мудака")},
    {"word": " мудаку ", "lens": len("мудаку")},
    {"word": " мудаком ", "lens": len("мудаком")},
    {"word": " мудила ", "lens": len("мудила")},
    {"word": " мудило ", "lens": len("мудило")},
    {"word": " мудозвон ", "lens": len("мудозвон")},
    {"word": " гандон ", "lens": len("гандон")},
    {"word": " гандоны ", "lens": len("гандоны")},
    {"word": " гондон ", "lens": len("гондон")},
    {"word": " пидор ", "lens": len("пидор")},
    {"word": " пидора ", "lens": len("пидора")},
    {"word": " пидору ", "lens": len("пидору")},
    {"word": " пидором ", "lens": len("пидором")},
    {"word": " пидорас ", "lens": len("пидорас")},
    {"word": " пидорасы ", "lens": len("пидорасы")},
    {"word": " пидрила ", "lens": len("пидрила")},
    {"word": " пидр ", "lens": len("пидр")},
    {"word": " шлюха ", "lens": len("шлюха")},
    {"word": " шлюхи ", "lens": len("шлюхи")},
    {"word": " шлюху ", "lens": len("шлюху")},
    {"word": " шлюхой ", "lens": len("шлюхой")},
    {"word": " блядина ", "lens": len("блядина")},
    {"word": " сука ", "lens": len("сука")},
    {"word": " суки ", "lens": len("суки")},
    {"word": " суку ", "lens": len("суку")},
    {"word": " сукой ", "lens": len("сукой")},
    {"word": " сучара ", "lens": len("сучара")},
    {"word": " сучары ", "lens": len("сучары")},
    {"word": " тварь ", "lens": len("тварь")},
    {"word": " твари ", "lens": len("твари")},
    {"word": " тварью ", "lens": len("тварью")},
    {"word": " урод ", "lens": len("урод")},
    {"word": " урода ", "lens": len("урода")},
    {"word": " уроды ", "lens": len("уроды")},
    {"word": " уродом ", "lens": len("уродом")},
    {"word": " дебил ", "lens": len("дебил")},
    {"word": " дебила ", "lens": len("дебила")},
    {"word": " дебилы ", "lens": len("дебилы")},
    {"word": " дебилом ", "lens": len("дебилом")},
    {"word": " идиот ", "lens": len("идиот")},
    {"word": " идиота ", "lens": len("идиота")},
    {"word": " идиоты ", "lens": len("идиоты")},
    {"word": " кретин ", "lens": len("кретин")},
    {"word": " кретина ", "lens": len("кретина")},
    {"word": " кретины ", "lens": len("кретины")},
    {"word": " даун ", "lens": len("даун")},
    {"word": " дауна ", "lens": len("дауна")},
    {"word": " дауны ", "lens": len("дауны")},
    {"word": " чмо ", "lens": len("чмо")},
    {"word": " чмошник ", "lens": len("чмошник")},
    {"word": " лох ", "lens": len("лох")},
    {"word": " лоха ", "lens": len("лоха")},
    {"word": " лохи ", "lens": len("лохи")},
    {"word": " лохом ", "lens": len("лохом")},
    {"word": " нацист ", "lens": len("нацист")},
    {"word": " нациста ", "lens": len("нациста")},
    {"word": " нацисты ", "lens": len("нацисты")},
    {"word": " фашист ", "lens": len("фашист")},
    {"word": " фашиста ", "lens": len("фашиста")},
    {"word": " фашисты ", "lens": len("фашисты")},
    {"word": " фашизм ", "lens": len("фашизм")},
    {"word": " нацизм ", "lens": len("нацизм")},
    {"word": " гитлерюгенд ", "lens": len("гитлерюгенд")},
    {"word": " свастика ", "lens": len("свастика")},
    {"word": " свастику ", "lens": len("свастику")},
    {"word": " свастикой ", "lens": len("свастикой")},
]


import re
from typing import Optional


class FubChecker:
    _OBFUSCATION = re.compile(r"[\*\.\-_|/\\0-9]+")

    _HOMOGLYPHS = str.maketrans({
        "x": "х", "o": "о", "a": "а", "e": "е", "p": "р",
        "c": "с", "y": "у", "k": "к", "m": "м", "t": "т",
        "h": "н", "b": "в", "u": "и",
    })

    _PUNCT = re.compile(r"[^\w\s]", re.UNICODE)

    def __init__(self, text: str):
        self.text = text
        self._norm = self._normalize(text)
        self._bad = [
            (self._normalize(w["word"]).strip(), int(w["lens"]))
            for w in bad_words
        ]

    def _normalize(self, s: str) -> str:
        s = s.lower()
        s = s.translate(self._HOMOGLYPHS)
        s = self._OBFUSCATION.sub("", s)
        s = self._PUNCT.sub(" ", s)
        s = re.sub(r"\s+", " ", s)
        return s

    def is_bad(self) -> bool:
        return any(word and word in self._norm for word, _ in self._bad)

    def replace_bad_on_star(self) -> Optional[str]:
        norm = self._norm
        replaced_any = False

        for word, lens in sorted(self._bad, key=lambda x: -len(x[0])):
            if not word:
                continue
            if word in norm:
                norm = norm.replace(word, " " + "*" * lens + " ")
                replaced_any = True

        if not replaced_any:
            return None

        self._norm = norm
        self.text = norm
        return self.text

    def replace_bad_on_star_preserve(self) -> Optional[str]:
        pattern_parts = []
        for word, lens in self._bad:
            if not word:
                continue
            esc = r"[\*\.\-_|/\\0-9]*".join(map(re.escape, word))
            pattern_parts.append((esc, lens))

        if not pattern_parts:
            return None

        combined = "|".join(f"(?P<w{i}>{p})" for i, (p, _) in enumerate(pattern_parts))
        rx = re.compile(combined, re.IGNORECASE)

        homoglyph_fixed = self.text.translate(self._HOMOGLYPHS)

        result = []
        last = 0
        found = False
        for m in rx.finditer(homoglyph_fixed):
            idx = next(i for i in range(len(pattern_parts)) if m.group(f"w{i}"))
            lens = pattern_parts[idx][1]
            result.append(self.text[last:m.start()])
            result.append(" " + "*" * lens + " ")
            last = m.end()
            found = True
        result.append(self.text[last:])

        if not found:
            return None
        self.text = "".join(result)
        self._norm = self._normalize(self.text)
        return self.text