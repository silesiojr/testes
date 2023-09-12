from flask import Flask, render_template, request, redirect
from docxtpl import DocxTemplate
from datetime import datetime
from babel.dates import format_date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/create_contract', methods=['POST'])
def create_contract():
    opcao1 = request.form['opcao1']                  #1
    opcao2 = request.form['opcao2']                  #2
    opcao3 = request.form['opcao3']                  #3
    opcao4 = request.form['opcao4']                  #4
    densidade = request.form['densidade']            #5
    edificacao = request.form['edificacao']          #6
    obraedificacao = request.form['obraedificacao']  #7
    ross= request.form['ross']                       #8
    ocupacao = request.form['ocupacao']              #9
    ocupante = request.form['ocupante']             #10
    relevo = request.form['relevo']                 #11
    tipoedificacao = request.form['tipoedificacao'] #12
    dia = request.form['dia']                       #13
    mes = request.form['mes']                       #14
    mesn = request.form['mesn']                     #15


    endereco = request.form['endereco']
    cidade = request.form['cidade']
    ano_atual = request.form['ano_atual']
    contratante = request.form['contratante']
    cpfcontratante = request.form['cpfcontratante']

    end_contratante = request.form['end_contratante']
    end_obra = request.form['end_obra']
    proprietario = request.form['proprietario']
    cpf_proprietario = request.form['cpf_proprietario']
    end_proprietario = request.form['end_proprietario']
    cep_proprietario = request.form['cep_proprietario']
    acompanhante = request.form['acompanhante']
    cpf_acompanhante = request.form['cpf_acompanhante']
    telefone_acompanhante = request.form['telefone_acompanhante']

    horario = request.form['horario']
    lote_vistoria = request.form['lote_vistoria']
    quadra_vistoria = request.form['quadra_vistoria']
    lote_obra = request.form['lote_obra']
    quadra_obra = request.form['quadra_obra']
    metragem = request.form['metragem']
    largura_via = request.form['largura_via']
    largura_testada = request.form['largura_testada']
    dist_obra = request.form['dist_obra']
    area_construida = request.form['area_construida']
    pe_direito = request.form['pe_direito']
    estrutura = request.form['estrutura']
    idade_aparente = request.form['idade_aparente']
    bairros_viz = request.form['bairros_viz']
    dist_centro = request.form['dist_centro']
    art = request.form['art']
    ambiente1 = request.form['ambiente1']
    ambiente2 = request.form['ambiente2']
    ambiente3 = request.form['ambiente3']
    ambiente4 = request.form['ambiente4']
    ambiente5 = request.form['ambiente5']
    ambiente6 = request.form['ambiente6']
    ambiente7 = request.form['ambiente7']
    ambiente8 = request.form['ambiente8']
    ambiente9 = request.form['ambiente9']
    ambiente10 = request.form['ambiente10']
    ambiente11 = request.form['ambiente11']
    ambiente12 = request.form['ambiente12']
    ambiente13 = request.form['ambiente13']
    ambiente14 = request.form['ambiente14']
    ambiente15 = request.form['ambiente15']

    # Adicione mais campos conforme necessário

    # Obtém a data atual em português-br
    data_atual = format_date(datetime.now(), format='long', locale='pt_BR')

    # Crie um contexto com os valores do formulário
    context = {
        'OPCAO1': opcao1,      #1
        'OPCAO2': opcao2,      #2
        'OPCAO3': opcao3,      #3
        'OPCAO4': opcao4,      #4
        'DENSIDADE': densidade,      #5
        'EDIFICAÇÃO': edificacao,      #6
        'OBRAEDIFICAÇÃO': obraedificacao,      #7
        'ROSS': ross,      #8
        'OCUPAÇÃO': ocupacao,      #9
        'OCUPANTE': ocupante,      #10
        'RELEVO': relevo,      #11
        'TIPOEDIFICAÇÃO': tipoedificacao,      #12
        'DIA': dia,      #13
        'MÊS': mes,      #14
        'MESN': mesn,      #15
        'DATAATUAL': data_atual,




        'ENDEREÇO': endereco,
        'CIDADE': cidade,
        'ANO': ano_atual,
        'CONTRATANTE': contratante,
        'CPFCONTRATANTE': cpfcontratante,
        'ENDCONTRATANTE': end_contratante,
        'ENDEREÇOOBRA': end_obra,
        'PROPRIETÁRIO': proprietario,
        'CPFPROPRIETÁRIO': cpf_proprietario,
        'ENDPROPRIETÁRIO': end_proprietario,
        'CEPPROPRIETÁRIO': cep_proprietario,
        'ACOMPANHANTE': acompanhante,
        'CPFACOMPANHANTE': cpf_acompanhante,
        'TELEFONEACOMPANHANTE': telefone_acompanhante,

        'HORÁRIO': horario,
        'LOTEVISTORIA': lote_vistoria,
        'QUADRAVISTORIA': quadra_vistoria,
        'LOTEOBRA': lote_obra,
        'QUADRAOBRA': quadra_obra,
        'METRAGEM': metragem,
        'LARGURAVIA': largura_via,
        'LARGURATESTADA': largura_testada,
        'DISTOBRA': dist_obra,
        'ÁREACONSTRUIDA': area_construida,
        'PÉ': pe_direito,
        'ESTRUTURA': estrutura,
        'IDADEAPARENTE': idade_aparente,
        'BAIRROSVIZ': bairros_viz,
        'DISTCENTRO': dist_centro,
        'ART': art,
        'AMBIENTE1': ambiente1,
        'AMBIENTE2': ambiente2,
        'AMBIENTE3': ambiente3,
        'AMBIENTE4': ambiente4,
        'AMBIENTE5': ambiente5,
        'AMBIENTE6': ambiente6,
        'AMBIENTE7': ambiente7,
        'AMBIENTE8': ambiente8,
        'AMBIENTE9': ambiente9,
        'AMBIENTE10': ambiente10,
        'AMBIENTE11': ambiente11,
        'AMBIENTE12': ambiente12,
        'AMBIENTE13': ambiente13,
        'AMBIENTE14': ambiente14,
        'AMBIENTE15': ambiente15,

        # Adicione mais campos ao contexto conforme necessário
    }

    # Carregue o template do documento
    doc = DocxTemplate('Parte 1.docx')

    # Renderize o documento com o contexto
    doc.render(context)

    # Salve o documento renderizado
    output_path = f'{contratante}-Contrato.docx'
    doc.save(output_path)

    return redirect('/success')

@app.route('/success')
def success():
    return 'Documento criado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)