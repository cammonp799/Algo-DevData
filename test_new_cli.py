"""Script de test pour vérifier la nouvelle fonctionnalité CLI."""

import sys
import subprocess

def test_cli_features():
    """Teste les nouvelles fonctionnalités CLI."""

    project_dir = "/Users/juniorchimene/PycharmProjects/project_weather_toulouse"

    tests = [
        ("Liste des stations", [
            "python3", "meteo_toulouse/main.py", "--list"
        ]),
        ("Récupérer 5 records", [
            "python3", "meteo_toulouse/main.py",
            "--station", "Paul Sabatier",
            "--limit", "5"
        ]),
        ("Avec raccourci -s", [
            "python3", "meteo_toulouse/main.py",
            "-s", "paul",
            "--limit", "3"
        ]),
        ("Mode verbeux", [
            "python3", "meteo_toulouse/main.py",
            "-s", "paul",
            "--limit", "2",
            "-v"
        ]),
        ("Afficher l'aide", [
            "python3", "meteo_toulouse/main.py",
            "--help"
        ])
    ]

    print("=" * 70)
    print("🧪 TESTS DES NOUVELLES FONCTIONNALITÉS CLI")
    print("=" * 70)
    print()

    for test_name, cmd in tests:
        print(f"\n{'=' * 70}")
        print(f"📝 {test_name}")
        print(f"{'=' * 70}")
        print(f"Commande: {' '.join(cmd)}")
        print()

        try:
            result = subprocess.run(
                cmd,
                cwd=project_dir,
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                print("✅ SUCCÈS")
                print()
                print(result.stdout[:500])  # Afficher les 500 premiers caractères
                if len(result.stdout) > 500:
                    print("... (résultat tronqué)")
            else:
                print("❌ ERREUR")
                print(result.stderr)

        except subprocess.TimeoutExpired:
            print("⏱️  TIMEOUT - La requête a dépassé 10 secondes")
        except Exception as e:
            print(f"💥 ERREUR: {e}")

    print()
    print("=" * 70)
    print("✅ TESTS TERMINÉS")
    print("=" * 70)


if __name__ == "__main__":
    test_cli_features()
