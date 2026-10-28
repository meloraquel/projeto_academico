# projeto_academico
Projeto Acadêmico
Atividade referente à aula 9 
Programação Python - Django - Configuração e Modelos básicos de ORM
Resumo e exercício de fixação
Nesta aula, você aprendeu que ORM é uma técnica para mapear classes e objetos para tabelas e registros de um banco relacional. No Django, os modelos são classes Python que herdam de models.Model, e seus atributos representam campos da tabela. 

Você também conheceu o padrão Active Record em uma aplicação prática: os objetos dos modelos podem ser salvos e alterados com save(), removidos com delete(), e consultados por meio do manager objects. Aprendeu ainda a diferença entre makemigrations, que cria o plano de alteração, e migrate, que aplica esse plano ao banco. 

O estudo de caso apresentou os modelos Curso e Aluno, incluindo uma relação muitos-para-um com ForeignKey. Por fim, os modelos foram registrados no Django Admin para permitir o gerenciamento dos dados por uma interface pronta. Exercício de fixação: crie um modelo Disciplina com os campos nome, codigo, carga_horaria e ativa. 

Depois, crie uma relação entre Disciplina e Curso, de modo que um curso possa possuir várias disciplinas. Gere e aplique as migrações, registre o novo modelo no admin e cadastre pelo menos duas disciplinas. 

No shell do Django, faça uma consulta que liste apenas as disciplinas ativas de um curso escolhido.

