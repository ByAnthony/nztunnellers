import { Menu } from '../Menu/Menu';
import STYLES from './HomePage.module.scss';

export function HomePage() {
  return (
    <div className={STYLES.homepage}>
      <Menu />
      <div className={STYLES.main}>
        <div>
          History
        </div>
        <div>
          Tunnellers
        </div>
      </div>
    </div>
  );
}
