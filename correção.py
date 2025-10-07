class GeradorRelatorio:
    def gerar(self, *args, titulo=None, rodape="Relatório gerado automaticamente", **kwargs):
        relatorio = ""
        if titulo:
            relatorio += f"# {titulo}\n\n"

        for paragrafo in args:
            relatorio += f"{paragrafo}\n"

        if kwargs:
            relatorio += "\n---\n**Metadados:**\n"
            for chave, valor in kwargs.items():
                relatorio += f"- **{chave.capitalize()}:** {valor}\n"

        relatorio += f"\n---\n* {rodape} *"
        
        return relatorio