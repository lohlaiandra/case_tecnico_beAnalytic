# case_tecnico_beAnalytic
teste extração de dados da steamdb via api

ao iniciar as opções de extração da pagina web steamdb, precebi que não seria possivel fazer atraves de um web scraping, pois a pagina contem restrições para esse tipo de extração, então recorri as apis disponibilizadas na pagina da mesma, tratei a requisição, o transformei em um dataframe usando pandas e enviei para o bigquery usando a biblioteca pandas_gbq.
