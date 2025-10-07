class GeradorRelatorio:
    def gerar(self, *args, rodape=None, **kwargs ):
        relatorio = ""

        match len(args):
            case 0:
                relatorio += '[Relatorio Vazio]\n'
            
            case 1:
                #apenas corpo do texto
                relatorio += f'{args[0]}\n'

            case 2:
                #titulo + corpo do texto 
                relatorio += f'=== {args[0]} ===\n'
                relatorio += f'{args[1]}\n'

            case _:
                # Título + múltiplos parágrafos
                relatorio += f"=== {args[0]} ===\n"
                for paragrafo in args[1:]:
                    relatorio += f"{paragrafo}\n\n"

        if rodape:
            relatorio += f'--- [rodape] ---\n'

        if kwargs:
            relatorio += '\n[Metadados]\n'
            for chave, valor in kwargs.items():
                relatorio += f'{chave.capitalize()}: {valor} \n'
        return relatorio.strip()
            

#-------------------------------------------------------------------------------------------------------
relatorio1 = GeradorRelatorio().gerar(
    "Este é o corpo do relatório simples. Ele apresenta uma visão geral das atividades realizadas no último mês, com foco nos indicadores de desempenho e metas atingidas.")

relatorio2 = GeradorRelatorio().gerar(
    "Relatório de Vendas",
    "Durante o mês de setembro, observamos um crescimento de 12% nas vendas em relação ao mês anterior. Os produtos mais vendidos foram os da categoria eletrônicos."
)

relatorio3 = GeradorRelatorio().gerar(
    "Relatório Financeiro",
    "O balanço financeiro do terceiro trimestre demonstra estabilidade nas receitas e leve redução nas despesas operacionais.",
    rodape="Documento confidencial — uso interno apenas"
)

relatorio4 = GeradorRelatorio().gerar(
    "Relatório de Estoque",
    "Parágrafo 1: O estoque atual apresenta níveis adequados para atender à demanda dos próximos dois meses.",
    "Parágrafo 2: Produtos com baixa rotatividade foram identificados e serão incluídos em campanhas promocionais.",
    "Parágrafo 3: A previsão de reposição está alinhada com o calendário de fornecedores."
)

relatorio5 = GeradorRelatorio().gerar(
    "Relatório Técnico",
    "Este relatório apresenta os resultados dos testes de desempenho realizados na nova versão do sistema.",
    "Os testes incluíram simulações de carga, análise de tempo de resposta e verificação de estabilidade.",
    rodape="Rodapé técnico — versão beta",
    autor="Katrina",
    data="07/10/2025",
    versao="1.0"
)

print(relatorio1)
print(relatorio2)
print(relatorio3)
print(relatorio4)
print(relatorio5)