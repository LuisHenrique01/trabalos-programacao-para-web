```python
 from core.models import *
 
 user1 = Usuario(email='luis@gmail.com', senha='Teste', data_nascimento='2020-01-12')
 
 user1.save()
 
 luis = Perfil(usuario=user1, nome='Luis')
 
 luis.save()
 
 henrique = Perfil(usuario=user1, nome='Henrique')
 
 henrique.save()
 
 luis.contatos.add(henrique)
 
 henrique.contatos.add(luis)
 
 p1 = Postagem(texto='Teste 01', perfil=luis)
 
 p1.save()
 
 p2 = Postagem(texto='Teste 02', perfil=luis)
 
 p2.save()
 
 p3 = Postagem(texto='Teste 03', perfil=luis)
 
 p3.save()
 
 p4 = Postagem(texto='Teste 04', perfil=henrique)
 
 p4.save()
 
 p5 = Postagem(texto='Teste 05', perfil=henrique)
 
 p5.save()
 
 c1 = Comentario(texto='Comentario 01', perfil=henrique, postagem=p1)
 
 c1.save()
 
 c2 = Comentario(texto='Comentario 02', perfil=henrique, postagem=p1)
 
 c2.save()
 
 c3 = Comentario(texto='Comentario 03', perfil=luis, postagem=p1)
 
 c3.save()
 
 r1 = Reacao(tipo='AMAR', postagem=p1, perfil=luis, peso=10)
 
 r1.save()
 
 r2 = Reacao(tipo='RIR', postagem=p1, perfil=henrique, peso=5)
 
 r2.save()
 
 luis.get_timeline()
 <QuerySet [<Postagem: Teste 01>, <Postagem: Teste 02>, <Postagem: Teste 03>]>
 
 henrique.get_timeline()
 <QuerySet [<Postagem: Teste 04>, <Postagem: Teste 05>]>
 
 p1.get_count_reacoes()
 <QuerySet [<Reacao: AMAR>, <Reacao: RIR>]>
 
 amar, rir = p1.get_count_reacoes()
 
 amar
 <Reacao: AMAR>
 
 amar.count_reacao
 10
 
 rir.count_reacao
 5
```