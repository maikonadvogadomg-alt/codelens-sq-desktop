#!/usr/bin/env python3
"""
Script para converter PNG para ICO, ICNS e PNG
Requer: pip install Pillow
"""

from PIL import Image
import os

def create_icons():
    # Ler a imagem original
    img = Image.open('public/icons/icon-512.png')
    
    # Criar pasta assets se não existir
    os.makedirs('assets', exist_ok=True)
    
    # Windows ICO (múltiplos tamanhos)
    print("🔄 Convertendo para Windows ICO...")
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icons = [img.resize(size, Image.Resampling.LANCZOS) for size in icon_sizes]
    icons[0].save(
        'assets/icon.ico',
        format='ICO',
        sizes=icon_sizes
    )
    print("✅ assets/icon.ico criado")
    
    # macOS ICNS
    print("🔄 Convertendo para macOS ICNS...")
    img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_resized.save('assets/icon.icns', format='ICNS')
    print("✅ assets/icon.icns criado")
    
    # Linux PNG
    print("🔄 Copiando para Linux PNG...")
    img.save('assets/icon.png', format='PNG')
    print("✅ assets/icon.png criado")
    
    print("\n✨ Todos os ícones foram criados com sucesso!")

if __name__ == '__main__':
    create_icons()