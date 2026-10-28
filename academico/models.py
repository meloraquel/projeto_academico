from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    carga_horaria = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "curso"
        verbose_name_plural = "cursos"
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="alunos",
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["nome"]
        verbose_name = "aluno"
        verbose_name_plural = "alunos"
    def __str__(self):
        return f"{self.nome} - {self.matricula}"

class Disciplina(models.Model):
    nome = models.CharField(max_length=120) #Neste campo o nome da disciplina é guardado em um campo de até 120 caracteres
    codigo = models.CharField(max_length=20, unique=True) # Este campo recebe caracteres e como o unique é verdadeiro, logo ele é único para cada disciplina cadastrada, logo ele será considerado como um atributo identificador da disciplina.
    carga_horaria = models.PositiveIntegerField(default=0) #Os valor recebido neste campo será sempre positivo pois serão consideradas as horas de duração da disciplina, dessa forma foi atribuído um valor padrão para o campo como "0", para que ele nunca retorne um valor vazio para o bando de dados, caso não seja estipulado uma carga horária para a disciplina.
    ativa = models.BooleanField(default=True) # Neste campo será definido se é ativo ou não a disciplina através de um booleano, que identifica se é verdadeiro ou falso.
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="disciplinas",
    ) #Como um curso pode ter várias disciplinas, logo a chave estrangeira dos cursos serão agregadas aos valores das disciplinas, visto que muitas disciplinas podem ter o mesmo curso.
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "disciplina"
        verbose_name_plural = "disciplinas"

    def __str__(self):
        return f"{self.nome} - {self.codigo}"