import pypdf
import numpy
import matplotlib
import math

"""
Carga =350000 N
n_cabos =8
vão = 15m
H = 12m
Grav = 9.81 m/s²
n_mean_rolamento = 98% e 99%
"""


class Redutor:
    def reduction_factor(self, w_motor=None, w_tambor=None, i=None):
        """
        Calcula o fator de redução de velocidade
        Equação original
            i = w_motor / w_tambor
        Equação para calcular w_motor
            w_motor = i * w_tambor
        Equação para calcular w_tambor
            w_tambor = w_motor / i    
        """
        if w_motor is None:
            print("Calculando w_motor: ")
            w_motor = i * w_tambor
            print("w_motor = ", w_motor)
            return w_motor / (w_tambor)
        elif w_tambor is None:
            print("Calculando w_tambor: ")
            w_tambor = w_motor / i
            print("w_tambor = ", w_tambor)
            return w_motor / (w_tambor)
        elif i is None:
            print("Calculando i: ")
            i = w_motor / w_tambor
            print("i = ", i)

    def v_tangencial(self, w=None, r=None, v_tang = None) -> float:
        """Calcula a velocidade tangencial, angular ou o raio com base no input da função:

        Equação original:
            v_tang = w * r

        Args:
            w (float): Velocidade Angular, em rad/s;
            r (float): Raio, em metros
            v_tang (float): Velocidade Tangencial, em m/s

        Returns:
            float: Depende do input
        """    
        if w is None:
            print("Calculando w: ")
            w = v_tang / r
            print("w = ", w)
            return w
        elif r is None:
            print("Calculando r: ")
            r = v_tang / w
            print("r = ", r)
            return r
        elif v_tang is None:
            print("Calculando v_tang: ")
            v_tang = w * r
            print("v_tang = ", v_tang)
            return v_tang

    def v_cabo(self, n_cabos=8, v_elev = None, v_cabo = None):
        """Calcuya a velocidade do cabo com base no número de cabos, velocidade de elevação e velocidade do cabo
        Dependendo do input, pode calcular o número de cabos, velocidade de elevação ou velocidade do cabo.

        Equação original:
            v_cabo = n_cabos/2 * v_elev
        Args:
            n_cabos (_type_, optional): _description_. Defaults to None.
            v_elev (_type_, optional): _description_. Defaults to None.
            v_cabo (_type_, optional): _description_. Defaults to None.
        """    
        if v_cabo is None:
            print("Calculando Velocidade do Cabo: ")
            v_cabo = (n_cabos/2) * v_elev
            print("v_cabo = ", v_cabo)
            return v_cabo
        elif n_cabos is None:
            print("Calculando Número de Cabos: ")
            n_cabos = (2 * v_cabo) / v_elev
            print("n_cabos = ", n_cabos)
            return n_cabos
        elif v_elev is None:
            print("Calculando Velocidade de Elevação: ")
            v_elev = (2 * v_cabo) / n_cabos
            print("v_elev = ", v_elev)
            return v_elev

    def rad_to_rpm(rad):
        """Converte rad/s para rpm

        Args:
            rad (float): Velocidade Angular em rad/s

        Returns:
            float: Velocidade Angular em rpm
        """    
        return rad * 9.5493

    def rpm_to_rad(rpm):
        """Converte rpm para rad/s

        Args:
            rpm (float): Velocidade Angular em rpm

        Returns:
            float: Velocidade Angular em rad/s
        """    
        return rpm * 0.10472

    def pot_term_geral(self, ptg= None, fa= None, fb=None, fc= None, ft= None, pt = None):
        """Utilizado para calcular a Potência Térmica Geral, Fator de Atividade, Fator de Beneficiamento, Fator de Carga, Fator de Tempo ou Potência Térmica Não Corrigida.
                PT = PTG * FA * FB * FC * FT

        """
        if pt is None:
            print("Calculando Potência Térmica Geral: ")
            pt = ptg * fa * fb * fc * ft
            print("PT = ", pt)
            return pt
        elif ptg is None:
            print("Calculando Potência Térmica Nâo Corrigida: ")
            ptg = pt / (fa * fb * fc * ft)
            print("PTG = ", ptg)
            return ptg
class Moitao:  
    def moitao(n_rol=None, k=4, n_moit=None, n_cabos=8):
        """Calcula o número de roldanas, o coeficiente de atrito ou o número de moitões
            Equação original:
                n_moit = (1/k) *((1- (n_rol)^k)/(1-n_rol))
        Args:
            n_rol (float, optional): Número de roldanas. Defaults to None.
            k (float, optional): Coeficiente de atrito. Defaults to None.
            n_moit (float, optional): Número de moitões. Defaults to None.
        """
        if n_moit is None:
            print("Calculando Eficiência do Moitão: ")
            n_moit = (1/k) *((1- (n_rol)**k)/(1-n_rol))
            print(f"Eficência do Moitão = {100*(n_moit):.2f}%")
            return n_rol
        elif n_rol is None:
            print("Calculando Número de Roldanas: ")
            n_rol = (1/k) *((1- (n_moit)^k)/(1-n_moit))
            return n_rol
        elif k is None:
            print("Calculando K:")
            k = (n_cabos)/2
            return k
        elif n_cabos is None:
            print("Calculando Número de Cabos:")
            n_cabos = 2 * k
            return n_cabos
class Cabo: # n_cabos = 8
    def tensao_cabo(self, Q=None, g_moit=None, n_cabos= 8 , n_moit=None, t_cabo=None):
        """Calcula a tensão no cabo com base na carga, gravidade, número de cabos, número de moitões e tensão do cabo

        Args:
            Q (float): Carga, em N
            g_moit (float): Gravidade do Moitão, em m/s²
            n_cabos (float): Número de Cabos
            n_moit (float): Número de Moitões
            tens_cabo (float): Tensão do Cabo, em N/m²

        Returns:
            float: Tensão no Cabo, em N/m²
        """    
        if t_cabo is None:
            print("Calculando Tensão no Cabo: ")
            t_cabo = (Q + g_moit) / (n_cabos * n_moit)
            print("Tensão no Cabo = ", t_cabo)
            return t_cabo
        elif Q is None:
            print("Calculando Carga: ")
            Q = (t_cabo * n_cabos * n_moit) - g_moit
            print("Carga = ", Q)
            return Q
        elif g_moit is None:
            print("Calculando Peso do Moitão: ")
            g_moit = (t_cabo * n_cabos * n_moit) - Q
            print("Gravidade do Moitão = ", g_moit)
            return g_moit
        elif n_cabos is None:
            print("Calculando Número de Cabos: ")
            n_cabos = (Q + g_moit) / (t_cabo * n_moit)
            print("Número de Cabos = ", n_cabos)
            return n_cabos
        elif n_moit is None:
            print("Calculando Número de Moitões: ")
            n_moit = (Q + g_moit) / (t_cabo * n_cabos)
            print("Número de Moitões = ", n_moit)
            return n_moit

    def coef_safety(self, t_rupt, t_cabo):
        """Calcula o coeficiente de segurança com base na tensão de ruptura e tensão do cabo

        Args:
            t_rupt (float): Tensão de Ruptura, em N/m²
            t_cabo (float): Tensão do Cabo, em N/m²

        Returns:
            float: Coeficiente de Segurança
        """
        print("Calculando Coeficiente de Segurança: ")
        t = t_rupt / t_cabo
        print("Coeficiente de Segurança = ", t)
        return t
class Tambor:
    def d_tambor(self, H1, H2, dc):
        """Calcula o diâmetro do tambor com base na altura do cabo na primeira camada, altura do cabo na última camada e diâmetro do cabo

        Args:
            H1 (float): Altura do cabo na primeira camada, em m
            H2 (float): Altura do cabo na última camada, em m
            dc (float): Diâmetro do cabo, em m

        Returns:
            float: Diâmetro do Tambor, em m
        """
        print("Calculando Diâmetro do Tambor: ")
        d = H1 * H2 * dc
        print("Diâmetro do Tambor = ", d)
        return d

    def d_polia(self, H1, H2, dc):
        """Calcula o diâmetro da polia com base na altura do cabo na primeira camada, altura do cabo na última camada e diâmetro do cabo

        Args:
            H1 (float): Altura do cabo na primeira camada, em m
            H2 (float): Altura do cabo na última camada, em m
            dc (float): Diâmetro do cabo, em m

        Returns:
            float: Diâmetro da Polia, em m
        """
        print("Calculando Diâmetro da Polia: ")
        d = H1 * H2 * dc
        print("Diâmetro da Polia = ", d)
        return d

    def l_total(self, Ntr, p, a, a2):
        """Calcula o comprimento total do cabo com base no número de voltas no tambor, passo, altura do cabo na primeira camada e altura do cabo na última camada

        Args:
            Ntr (float): Número de Voltas no Tambor
            p (float): Passo, em m
            a (float): Altura do cabo na primeira camada, em m
            a2 (float): Altura do cabo na última camada, em m

        Returns:
            float: Comprimento Total do Cabo, em m
        """
        print("Calculando Comprimento Total do Cabo: ")
        l = (Ntr *p) + (a+1) + (2*a2)
        print("Comprimento Total do Cabo = ", l)
        return l

    def ntr(self, nru):
        """Calcula o número de voltas no tambor com base no número de roldanas de retorno

        Args:
            nru (float): Número de Roldanas de Retorno

        Returns:
            float: Número de Voltas no Tambor
        """
        print("Calculando Número de Voltas no Tambor: ")
        n = nru + 4
        print("Número de Voltas no Tambor = ", n)
        return n

    def nru(self, nc, H, d_t):
        """Calcula o número de roldanas de retorno com base no número de camadas, altura do cabo na última camada e diâmetro do tambor

        Args:
            nc (float): Número de Camadas
            H (float): Altura do cabo na última camada, em m
            d_t (float): Diâmetro do Tambor, em m

        Returns:
            float: Número de Roldanas de Retorno
        """
        print("Calculando Número de Roldanas de Retorno: ")
        n = (nc - H)/(math.pi - d_t)
        print("Número de Roldanas de Retorno = ", n)
        return n

class Tubo_chapa:
    def e_chapa(self, h1, h, sobremetal):
        """Calcula a espessura da chapa com base na altura da chapa, altura do tambor e sobremetal

        Args:
            h1 (float): Altura da Chapa, em m
            h (float): Altura do Tambor, em m
            sobremetal (float): Sobremetal, em m

        Returns:
            float: Espessura da Chapa, em m
        """
        print("Calculando Espessura da Chapa: ")
        e = h1 + h + sobremetal
        print("Espessura da Chapa = ", e)
        return e

    def a_chapa(self, a_corpo, a_ref):
        """Calcula a área da chapa com base na área do corpo e Área de Reforço

        Args:
            a_corpo (float): Área do Corpo, em m²
            a_ref (float): Área de Reforço, em m²

        Returns:
            float: Área da Chapa, em m²
        """
        print("Calculando Área da Chapa: ")
        a = a_corpo + a_ref
        print("Área da Chapa = ", a)
        return a
    
    def a_ref(self, dt):
        """Calcula a Área de Reforço com base no diâmetro do tambor e diâmetro da polia

        Args:
            d_t (float): Diâmetro do Tambor, em m
            d_p (float): Diâmetro da Polia, em m

        Returns:
            float: Área de Reforço, em m²
        """
        print("Calculando Área de Reforço: ")
        a = (math.pi * (dt**2))/4
        print("Área de Reforço = ", a)
        return a
    
    def a_corpo(self, dt, lt):
        """Calcula a Área do Corpo com base no diâmetro do tambor e comprimento total do cabo

        Args:
            dt (float): Diâmetro do Tambor, em m
            lt (float): Comprimento Total do Cabo, em m

        Returns:
            float: Área do Corpo, em m²
        """
        print("Calculando Área do Corpo: ")
        a = (math.pi * dt) * lt
        print("Área do Corpo = ", a)
        return a
    
    def g_tubo(self, chapa, m_chapa, g):
        """Calcula o peso do tubo com base na chapa, massa da chapa e gravidade

        Args:
            chapa (float): Espessura da Chapa, em m
            m_chapa (float): Massa da Chapa, em kg/m²
            g (float): Gravidade, em m/s²

        Returns:
            float: Peso do Tubo, em N
        """
        print("Calculando Peso do Tubo: ")
        p = chapa * m_chapa * g * 1.2
        print("Peso do Tubo = ", p)
        return p
    
class Motor:
    def p_nec(self, Q, g_moit, v_e, n_1, n_2):
        """Calcula a potência necessária com base na carga, peso do moitão, velocidade de elevação, número de polias no tambor e número de polias na polia

        Args:
            Q (float): Carga, em N
            g_moit (float): Peso do Moitão, em N
            v_e (float): Velocidade de Elevação, em m/s
            n_1 (float): Número de Polias no Tambor
            n_2 (float): Número de Polias na Polia

        Returns:
            float: Potência Necessária, em W
        """
        print("Calculando Potência Necessária: ")
        p = (((Q + g_moit) * v_e) / (n_1 * n_2))
        print("Potência Necessária = ", p)
        return p
    
    def pot(self, torque, rot):
        """Calcula a potência com base no torque e rotação

        Args:
            torque (float): Torque, em N.m
            rot (float): Rotação, em rpm

        Returns:
            float: Potência, em W
        """
        print("Calculando Potência: ")
        p = (torque * rot)
        print("Potência = ", p)
        return p
    
    def torque(self, F, r):
        """Calcula o torque com base na força e raio

        Args:
            F (float): Força, em N
            r (float): Raio, em m

        Returns:
            float: Torque, em N.m
        """
        print("Calculando Torque: ")
        t = (F * r)
        print("Torque = ", t)
        return t