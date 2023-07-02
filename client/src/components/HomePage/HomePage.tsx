import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
import STYLES from './HomePage.module.scss';

export function HomePage() {
  return (
    <>
      <Menu />
      <div className={STYLES.main}>
        <div>
          History
        </div>
        <div>
          Tunnellers
        </div>
      </div>
      <Footer />
    </>
  );
}
