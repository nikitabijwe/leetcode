class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)

        for domain in cpdomains:
            # Split the input string into count and domain
            count, domain = domain.split()
            count = int(count)

            # Split the domain into fragments
            fragments = domain.split('.')

            # Iterate over fragments and update counts for subdomains
            for i in range(len(fragments)):
                counts['.'.join(fragments[i:])] += count


        # Format the output as a list of strings "count domain"
        return [f"{count} {domain}" for domain, count in counts.items()]

