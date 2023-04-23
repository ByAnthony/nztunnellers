import { Link } from 'react-router-dom';
import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';

export function HomePage() {
  return (
    <>
      <Menu />
      <Link to="/roll" aria-label="Open the World War I timeline.">
        <div>
          <p>World War I (1914-1918)</p>
          <span>New Zealand Tunnellers</span>
        </div>
        {/* <div className={STYLES.arrow}>&rarr;</div> */}
      </Link>
      <Footer />
    </>
  );
}
