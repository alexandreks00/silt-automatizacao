class Empresa:
    def __init__(self, razao_social, fantasia, cnpj, tipo_inscricao, inscricao_estadual,
                 tipo, tipo_danfe, emite_nf, cep, numero, complemento,
                 entrega, cobranca, endereco_fiscal, impressao, armazem,
                 integracao_via_servico_rest, setor_armazenagem, codigo_integracao, area_setor,
                 tipo_setor, permite_expedicao_produto, permite_mais_produto_pulmao, depositante_ref):

        self.razao_social = razao_social
        self.fantasia = fantasia
        self.cnpj = cnpj
        self.tipo_inscricao = tipo_inscricao
        self.inscricao_estadual = inscricao_estadual
        self.tipo = tipo
        self.tipo_danfe = tipo_danfe
        self.emite_nf = emite_nf
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.entrega = entrega
        self.cobranca = cobranca
        self.endereco_fiscal = endereco_fiscal
        self.impressao = impressao
        self.armazem = armazem
        self.integracao_via_servico_rest = integracao_via_servico_rest
        self.depositante_ref = depositante_ref


class SetorI:
    def __init__(self, setor_armazenagem, codigo_integracao,
                 area_setor, tipo_setor, permite_expedicao_produto,
                 permite_mais_produto_pulmao, razao_social, regiao_armazenagem,	tipo_armazenagem, tipo_recebimento):

        self.setor_armazenagem = setor_armazenagem
        self.codigo_integracao = codigo_integracao
        self.area_setor = area_setor
        self.tipo_setor = tipo_setor
        self.permite_expedicao_produto = permite_expedicao_produto
        self.permite_mais_produto_pulmao = permite_mais_produto_pulmao
        self.razao_social = razao_social
        self.regiao_armazenagem = regiao_armazenagem
        self.tipo_armazenagem = tipo_armazenagem
        self.tipo_recebimento = tipo_recebimento


class DataFtp:
    def __init__(self, importacao, backup_importacao, exportacao, backup_exportacao, erro):
        self.importacao = importacao
        self.backup_importacao = backup_importacao
        self.exportacao = exportacao
        self.backup_exportacao = backup_exportacao
        self.erro = erro


class DataOr:
    def __init__(self, codigo_tipo_recebimento,	codigo_doca, placa_veiculo, quantidade_volume_recebido,	intervalo_integracao):
        self.codigo_tipo_recebimento = codigo_tipo_recebimento
        self.codigo_doca = codigo_doca
        self.placa_veiculo = placa_veiculo
        self.quantidade_volume_recebido = quantidade_volume_recebido
        self.intervalo_integracao = intervalo_integracao


class TipoPedidoI:
    def __init__(self, codigo_integracao, descricao, setor, situacao_lote, estado_material):
        self.codigo_integracao = codigo_integracao
        self.descricao = descricao
        self.setor = setor
        self.situacao_lote = situacao_lote
        self.estado_material = estado_material


class PadraoIntegracaoI:
    def __init__(self, tipo_palete_completo, tipo_palete_incompleto, tipo_palete_sobra,
                 tipo_palete_unidade, quantidade_maxima_picking, ativo,	picking_dinamico,
                 aceita_qualquer_barra, percentual_capacidade, coleta_lote_industria,	coletar_vencimento_lote
                 ):

        self.tipo_palete_completo = tipo_palete_completo
        self.tipo_palete_incompleto = tipo_palete_incompleto
        self.tipo_palete_sobra = tipo_palete_sobra
        self.tipo_palete_unidade = tipo_palete_unidade
        self.quantidade_maxima_picking = quantidade_maxima_picking
        self.ativo = ativo
        self.picking_dinamico = picking_dinamico
        self.aceita_qualquer_barra = aceita_qualquer_barra
        self.percentual_capacidade = percentual_capacidade
        self.coleta_lote_industria = coleta_lote_industria
        self.coletar_vencimento_lote = coletar_vencimento_lote


class SetorPadraoI:
    def __init__(self, doca, bancada, prefix):
        self.doca = doca
        self.bancada = bancada
        self.prefix = prefix

class TransportadoraI:
    def __init__(self, codigo_servico, codigo_servico_exportacao, descricao, codigo_servico_adicionais,
                 numero_cartao, codigo_unidade, unidade_postagem, orgao_credenciado, dr_postagem,
                 unidade, endereco, modelo_etiqueta, razao_social, cnpj_transportadora):

        self.codigo_servico = codigo_servico
        self.codigo_servico_exportacao = codigo_servico_exportacao
        self.descricao = descricao
        self.codigo_servico_adicionais = codigo_servico_adicionais
        self.numero_cartao = numero_cartao
        self.codigo_unidade = codigo_unidade
        self.unidade_postagem = unidade_postagem
        self.orgao_credenciado = orgao_credenciado
        self.dr_postagem = dr_postagem
        self.unidade = unidade
        self.endereco = endereco
        self.modelo_etiqueta = modelo_etiqueta
        self.razao_social = razao_social
        self.cnpj_transportadora = cnpj_transportadora