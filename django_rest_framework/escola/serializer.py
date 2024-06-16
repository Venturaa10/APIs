# Arquivo que servira como filtro dos dados que eu quero disponibilizar para a API
# Configura a forma em que as informações dos objetos cadastrados serão exibidos no Django REST Framework
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' 

# all -> Informa que quero exibir todos os campos/atributos de curso

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] 
    

# exclude = ['id'] # Essa é uma outra forma de visualizar os campos, nesse caso o id será excluido e todos os outros campos poderam ser visualizados, no caso acima, como está sem nenhuma informação, será retornado todas as informações sem exclusão de nenhuma

class ListaMatriculasAlunosSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    # As linhas de acima estão configurando a maneira que será exibido o curso e o periodo no momento que exiibir o alunos e as matriculas do aluno
    # No curso está retornando a descrição do curso, em periodo é o significado da sigla , exemplo: 'M' vai exibir 'Matutino'
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome') # Será exibido o nome do Aluno, e não o seu id
    class Meta:
        model = Matricula
        fields  = ['aluno_nome']