import STYLES from './Footer.module.scss';

export function Footer() {
  return (
    <div className={STYLES.footer}>
      <div>
        <a href="/" className={STYLES.logo} aria-label="Go to the Homepage."><img src="../nzt_logo.png" alt="" height={32} /></a>
      </div>
      <div>
        <div className={STYLES['footer-links-container']}>
          <div>
            <p>The Company History</p>
            <ul>
              <li>
                <a href="/history/call-to-pick-and-shovel/" aria-label="The history of the Company, Chapter 1: Call To Pick & Shovel.">Call To Pick & Shovel</a>
              </li>
              <li>
                <a href="/history/the-way-to-war/" aria-label="The history of the Company, Chapter 2: The Way To War.">The Way To War</a>
              </li>
              <li>
                <a href="/history/beneath-artois-fields/" aria-label="The history of the Company, Chapter 3: Beneath Artois Fields.">Beneath Artois Fields</a>
              </li>
              <li>
                <a href="/history/tunnelling-under-arras/" aria-label="The history of the Company, Chapter 4: Tunnelling Under Arras.">Tunnelling Under Arras</a>
              </li>
              <li>
                <a href="/history/always-digging/" aria-label="The history of the Company, Chapter 5: Always Digging.">Always Digging</a>
              </li>
              <li>
                <a href="/history/bridging-in-the-end/" aria-label="The history of the Company, Chapter 6: Bridging In The End.">Bridging In The End</a>
              </li>
              <li>
                <a href="/history/after-the-armistice/" aria-label="The history of the Company, Chapter 7: After The Armistice.">After The Armistice</a>
              </li>
            </ul>
          </div>
          <div>
            <p>Tunellers Stories</p>
            <ul>
              <li>
                <a href="/roll/" aria-label="The Company Roll: a list of the men who enlisted in the Company.">Company Roll</a>
              </li>
            </ul>
            <p>Website</p>
            <ul>
              <li>
                <a href="/about-us/" aria-label="About Us">About Us</a>
              </li>
              <li>
                <a href="/contact-us/" aria-label="Contact Us">Contact Us</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
