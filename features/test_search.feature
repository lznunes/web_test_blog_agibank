Feature: Pesquisa
    Pesquisa sentenca

    @busca @todos
    Scenario: Pesquisa de sentenca correta
        Given que acesso o blog
        When clica no botão de pesquisa
        And preenchido o input com a sentença correta
        And pressionado a tecla ENTER
        Then devo visualizar os resultados pesquisa correta
    
    @todos
    Scenario: Pesquisa de sentenca incorreta
        Given que acesso o blog
        When clica no botão de pesquisa
        And preenchido o input com a sentença incorreta
        And pressionado a tecla ENTER
        Then devo visualizar os resultados pesquisa incorreta

