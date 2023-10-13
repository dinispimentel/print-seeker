# print-seeker

Este projeto consistia numa demonstração de vulnerabilidade no sistema de upload de screenshots do [Lightshot](https://app.prntscr.com/en/index.html).

## Vulnerabilidade Explorada
A tool [Lightshot](https://app.prntscr.com/en/index.html) permite capturar e enviar prints para uma host pública, permitindo assim partilhá-la com pessoas. Contudo, a implementação do sistema de geração de links é falha, uma vez que são uma sequência previsível (https://prnt.sc/<num em base 36 \[0-z\]>).

Isto dito, é possível aceder a prints de outras pessoas sem ter o link previamente. Assim, com este "crawler", é-se possível passar por várias imagens e utilizar uma framework de OCR para filtrar imagens com certas _keywords_.


## Disclaimer

Todo o uso dado a este programa foi, é e será ético, não usufruindo dos dados sensíveis obtidos para proveito própio danoso.
