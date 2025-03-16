import hashlib
import os
import base64
import json
from cryptography.fernet import Fernet

class QuantumKeyDistributor:
    """
    Simula a distribuição de chaves quânticas (QKD) gerando e compartilhando chaves seguras.
    """
    def __init__(self):
        self.keys = {}
    
    def generate_key(self, system_id: str):
        key = Fernet.generate_key()
        self.keys[system_id] = key
        return key
    
    def get_key(self, system_id: str):
        return self.keys.get(system_id, None)

class SecureChannel:
    """
    Cria um canal de comunicação seguro utilizando chaves distribuídas pelo QKD.
    """
    def __init__(self, system_id: str, qkd: QuantumKeyDistributor):
        self.system_id = system_id
        self.qkd = qkd
        self.key = self.qkd.generate_key(system_id)
        self.cipher = Fernet(self.key)
    
    def encrypt_message(self, message: str) -> str:
        """Criptografa uma mensagem utilizando a chave quântica simulada."""
        return self.cipher.encrypt(message.encode()).decode()
    
    def decrypt_message(self, encrypted_message: str) -> str:
        """Descriptografa uma mensagem recebida."""
        return self.cipher.decrypt(encrypted_message.encode()).decode()
    
    def send_message(self, recipient_channel, message: str):
        """Envia uma mensagem criptografada para outro sistema."""
        encrypted_msg = self.encrypt_message(message)
        return recipient_channel.receive_message(encrypted_msg)
    
    def receive_message(self, encrypted_message: str):
        """Recebe uma mensagem e a descriptografa."""
        return self.decrypt_message(encrypted_message)

# Simulação de comunicação entre dois sistemas
if __name__ == "__main__":
    qkd = QuantumKeyDistributor()
    system_A = SecureChannel("SystemA", qkd)
    system_B = SecureChannel("SystemB", qkd)
    
    message = "Mensagem confidencial com criptografia quântica!"
    print(f"System A envia: {message}")
    
    encrypted_msg = system_A.send_message(system_B, message)
    print(f"System B recebe (criptografado): {encrypted_msg}")
    
    decrypted_msg = system_B.receive_message(encrypted_msg)
    print(f"System B decodificado: {decrypted_msg}")
