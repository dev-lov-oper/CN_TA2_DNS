#!/usr/bin/env python3
"""
DNS Threat Detection Demo Script
Generates traffic patterns to demonstrate Wireshark filter effectiveness
For educational purposes only - generates benign test traffic
"""

import socket
import time
import base64
import binascii
import random
import string
import dns.resolver
from datetime import datetime

class DNSThreatSimulator:
    def __init__(self):
        self.dns_servers = ['8.8.8.8', '1.1.1.1', '208.67.222.222']
        self.test_domains = ['example.com', 'test.com', 'simulation.local']

    def print_banner(self):
        print("="*70)
        print("🛡  DNS THREAT DETECTION DEMO GENERATOR")
        print("📊 Generates traffic for Wireshark filter demonstration")
        print("⚠  Educational purposes only - Safe simulation traffic")
        print("="*70)
        print(f"🕒 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

    def tunneling_simulation(self):
        """
        Generate DNS Tunneling patterns for filters:
        - dns and frame.len > 400
        - dns.qry.name matches "^[A-Za-z0-9+/]{40,}="
        """
        print("🚇 TUNNELING DETECTION SIMULATION")
        print("-" * 50)

        # Pattern 1: Large DNS packets (>400 bytes)
        print("📏 Generating large DNS packets (>400 bytes)...")

        large_payloads = [
            base64.b64encode(("tunneling_data_" * 20 + "secret_payload_information").encode()).decode() + ".tunnel-test.example.com",
            base64.b64encode(("exfiltration_simulation_" * 15 + "confidential_data_leak").encode()).decode() + ".covert-channel.test.com",
            base64.b64encode(("malicious_communication_" * 18 + "command_control_data").encode()).decode() + ".c2-simulation.local"
        ]

        for i, domain in enumerate(large_payloads, 1):
            print(f"   🎯 Query {i}: {domain[:60]}... ({len(domain)} chars)")
            try:
                resolver = dns.resolver.Resolver()
                resolver.timeout = 2
                resolver.resolve(domain, 'A')
            except Exception as e:
                pass
            time.sleep(1.5)

        # Pattern 2: Base64-like encoded domains
        print("\n🔤 Generating base64-pattern domains...")

        base64_domains = [
            "dGVzdGluZ0RhdGFGb3JUdW5uZWxpbmdEZXRlY3Rpb25UZXN0aW5nTG9uZ0RvbWFpbg==.example.com",
            "bXlzZWNyZXREYXRhRXhmaWx0cmF0aW9uU2ltdWxhdGlvblRlc3RpbmdEb21haW5OYW1l.test.com",
            "Y29tbWFuZENvbnRyb2xEYXRhVHVubmVsaW5nU2ltdWxhdGlvblRlc3RpbmdQYXlsb2Fk.simulation.local"
        ]

        for i, domain in enumerate(base64_domains, 1):
            print(f"   🎯 Query {i}: {domain}")
            try:
                resolver = dns.resolver.Resolver()
                resolver.timeout = 2
                resolver.resolve(domain, 'A')
            except:
                pass
            time.sleep(1)
        print("✅ Tunneling simulation completed\n")

    def spoofing_simulation(self):
        """
        Generate DNS Spoofing patterns for filters:
        - dns.flags.response == 1 and dns.count.answers > 1  
        - dns.resp.ttl < 60
        """
        print("🎭 SPOOFING DETECTION SIMULATION")
        print("-" * 50)

        # Pattern 1: Query domains likely to have multiple answers
        print("📊 Generating queries for multiple answer responses...")

        multi_answer_domains = [
            'google.com',
            'microsoft.com',
            'cloudflare.com',
            'amazon.com',
            'facebook.com'
        ]

        for domain in multi_answer_domains:
            print(f"   🎯 Querying: {domain}")
            try:
                answers = dns.resolver.resolve(domain, 'A')
                print(f"      📋 Received {len(answers)} A record answers")
            except Exception as e:
                print(f"      ❌ Error: {str(e)[:50]}")
            time.sleep(1)

        print("\n⏰ Querying services with potentially low TTL...")

        low_ttl_candidates = [
            'cdn.jsdelivr.net',
            'ajax.googleapis.com', 
            'fonts.gstatic.com',
            'assets.github.com',
            'api.github.com'
        ]

        for domain in low_ttl_candidates:
            print(f"   🎯 Querying: {domain}")
            try:
                dns.resolver.resolve(domain, 'A')
            except Exception as e:
                print(f"      ❌ Error: {str(e)[:50]}")
            time.sleep(1)
        print("✅ Spoofing simulation completed\n")

    def exfiltration_simulation(self):
        """
        Generate Data Exfiltration patterns for filters:
        - dns.qry.name matches ".[0-9a-f]{32,}."
        - dns.qry.type == 16
        """
        print("📤 DATA EXFILTRATION SIMULATION")
        print("-" * 50)

        # Pattern 1: Hexadecimal encoded data in domain names
        print("🔢 Generating hexadecimal pattern domains...")

        hex_domains = [
            "deadbeefcafebabe1234567890abcdef12345678.exfil-test.example.com",
            "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcd.data-leak.test.com", 
            "0123456789abcdef0123456789abcdef0123456789abcdef01234567.covert-exfil.local",
            "feedfacedeadbeefcafebabefeedface1234567890abcdef12345678.stealth-transfer.example.com"
        ]

        fake_data = ["user_credentials", "database_dump", "secret_keys", "confidential_files"]

        for i, (domain, data_type) in enumerate(zip(hex_domains, fake_data), 1):
            print(f"   🎯 Simulating {data_type} exfiltration...")
            print(f"      🔗 Domain: {domain[:70]}...")
            try:
                dns.resolver.resolve(domain, 'A')
            except:
                pass
            time.sleep(2)

        # Pattern 2: TXT record queries (common for exfiltration)
        print("\n📝 Generating TXT record queries...")

        txt_targets = [
            'google.com',
            'microsoft.com',
            'github.com',
            '_dmarc.gmail.com',
            '_spf.google.com',
            'cloudflare.com'
        ]

        for domain in txt_targets:
            print(f"   🎯 TXT query: {domain}")
            try:
                txt_records = dns.resolver.resolve(domain, 'TXT')
                print(f"      📋 Found {len(txt_records)} TXT records")
            except Exception as e:
                print(f"      ❌ Error: {str(e)[:50]}")
            time.sleep(1.5)
        print("✅ Exfiltration simulation completed\n")

    def generate_additional_patterns(self):
        """Generate additional suspicious patterns for comprehensive testing"""
        print("🔍 ADDITIONAL THREAT PATTERNS")
        print("-" * 50)

        # High entropy domain generation (DGA simulation)
        print("🎲 Generating high-entropy domains (DGA simulation)...")

        for i in range(3):
            random_domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=35))
            domain = f"{random_domain}.dga-simulation.example.com"
            print(f"   🎯 DGA Query {i+1}: {domain}")
            try:
                dns.resolver.resolve(domain, 'A')
            except:
                pass
            time.sleep(1)

        print("\n⚡ Generating rapid query patterns...")
        rapid_domains = [f"auto-query-{i}.rapid-test.example.com" for i in range(5)]
        for domain in rapid_domains:
            print(f"   🎯 Rapid query: {domain}")
            try:
                dns.resolver.resolve(domain, 'A')
            except:
                pass
            time.sleep(0.5)
        print("✅ Additional patterns completed\n")

    def run_full_simulation(self):
        """Run complete DNS threat simulation suite"""
        self.print_banner()

        print("🎮 Starting comprehensive DNS threat simulation...")
        print("📊 Make sure Wireshark is capturing on your network interface!")
        print("⏳ Each simulation will pause between queries for better analysis...")
        print()

        try:
            self.tunneling_simulation()
            time.sleep(2)
            self.spoofing_simulation() 
            time.sleep(2)
            self.exfiltration_simulation()
            time.sleep(2)
            self.generate_additional_patterns()
            print("🎉 SIMULATION SUITE COMPLETED!")
            print("="*70)
            print("📊 Now apply these Wireshark filters to see the results:")
            print()
            print("🚇 Tunneling Detection:")
            print('   dns and frame.len > 400')
            print('   dns.qry.name matches "^[A-Za-z0-9+/]{40,}="')
            print()
            print("🎭 Spoofing Detection:")  
            print('   dns.flags.response == 1 and dns.count.answers > 1')
            print('   dns.resp.ttl < 60')
            print()
            print("📤 Exfiltration Detection:")
            print('   dns.qry.name matches ".[0-9a-f]{32,}."') 
            print('   dns.qry.type == 16')
            print()
            print("✅ You should now see packets in Wireshark matching these filters!")
            print("="*70)

        except KeyboardInterrupt:
            print("\n🛑 Simulation stopped by user")
        except Exception as e:
            print(f"\n❌ Error during simulation: {e}")

if __name__ == "__main__":
    # Check for required dependencies
    try:
        import dns.resolver
        print("✅ dnspython library detected")
    except ImportError:
        print("❌ Missing dnspython library")
        print("   Install with: pip install dnspython")
        exit(1)
    # Initialize and run simulator
    simulator = DNSThreatSimulator()
    simulator.run_full_simulation()
