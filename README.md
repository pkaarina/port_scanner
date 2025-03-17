# Port Scanner - by Karina Ferreira

## Descrição
Este é um scanner de portas desenvolvido em Python que permite verificar o status de portas específicas em um host determinado. Ele utiliza threads para acelerar o processo e salva os resultados em um arquivo JSON.

## Tecnologias Utilizadas
- `Python 3`
- `socket` para conexão com as portas
- `json` para salvar os resultados
- `time` para medição do tempo de resposta
- `threading` para execução paralela
- `colorama` para realce de cores no terminal

## Como Usar

### 1. Instalar Dependências
Antes de executar o script, certifique-se de instalar a biblioteca `colorama`, caso ainda não tenha:
```bash
pip install colorama
```

### 2. Executar o Script
Execute o script Python:
```bash
python port_scanner.py
```

### 3. Inserir o Host
Ao iniciar o programa, ele solicitará que você insira um host ou um endereço IP para escanear.

### 4. Verificar os Resultados
O scanner irá analisar as portas predefinidas e exibir o status de cada uma (aberta ou fechada) juntamente com o tempo de resposta.

### 5. Salvar Resultados
Os resultados serão salvos automaticamente em um arquivo JSON com o nome:
```bash
<host>_scan_results.json
```

## Lista de Portas Escaneadas
O scanner verifica as seguintes portas conhecidas:

| Porta | Serviço |
|-------|---------|
| 21    | FTP     |
| 22    | SSH     |
| 23    | Telnet  |
| 25    | SMTP    |
| 53    | DNS     |
| 80    | HTTP    |
| 110   | POP3    |
| 143   | IMAP    |
| 443   | HTTPS   |
| 3306  | MySQL   |
| 3389  | RDP     |

## Exemplo de Saída
```bash
Digite o host ou IP para escanear: 198.0.0.0
Iniciando varredura no host 198.0.0.0...
Port 22 (SSH): open - Tempo de resposta: 2.5 ms
Port 80 (HTTP): closed - Tempo de resposta: 1.1 ms
Varredura concluída em 5.3 segundos.
Resultados salvos em 198.0.0.0_scan_results.json
```

# Contribuição

Sinta-se à vontade para contribuir com melhorias! Basta fazer um fork do repositório, criar uma branch com suas alterações e abrir um pull request.

