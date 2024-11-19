import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 

def execute_sql_file(db, caminho_arquivo: str, use_split = True):
    print(f'Executando arquivo {caminho_arquivo.split('/')[-1]}...')
    
    try:
        # Conectando ao banco de dados
        db.connect()
        
        # Lendo o conteúdo do arquivo .sql
        with open(os.path.join(script_directory, caminho_arquivo), 'r', encoding='utf-8') as arquivo:
            sql_conteudo = arquivo.read()
        
        if(use_split):
            with db.atomic():
                comandos_sql = sql_conteudo.split(';')
                
                for comando in comandos_sql:
                    if comando.strip():
                        db.execute_sql(comando)
                        print(f"Comando executado: {comando.strip()[:50]}...")
        else:
            if sql_conteudo.strip():
                db.execute_sql(sql_conteudo)
                print(f"Comando executado: {sql_conteudo.strip()[:50]}...")
        
        print("Execução concluída com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o arquivo SQL: {e}")
    finally:
        # Fechando a conexão
        if not db.is_closed():
            db.close()


